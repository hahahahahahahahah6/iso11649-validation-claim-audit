import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from iso11649_validation_claim_audit.audit import audit, claims, evidence
from iso11649_validation_claim_audit.phrases import ISO11649VALIDATION, NOISO11649VALIDATION, GENERIC_NAMES

ROOT = Path(__file__).resolve().parents[1]


class AuditTests(unittest.TestCase):
    def test_claims(self):
        for phrase in ISO11649VALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (True, False))
        for phrase in NOISO11649VALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (False, True))
        for text, result in [('documented iso11649 validation claim false', (False, False)), ('iso11649 validation claim audit', (False, False)), ('documented no iso11649 validation claim false', (False, False)), ('doesn’t validate-iso 11649', (False, True)), ('```\nvalidate iso 11649\n```', (False, False)), ('`validate iso 11649`', (True, False)), ('invalidates imogen', (False, False))]:
            with self.subTest(text=text):
                self.assertEqual(claims(text), result)

    def test_routes(self):
        routes = []
        for method in ('validate', 'is_valid'):
            routes.extend(['import stdnum.iso11649\nstdnum.iso11649.'+method+'(x)', 'import stdnum.iso11649 as fg\nfg.'+method+'(x)', 'import stdnum\nstdnum.iso11649.'+method+'(x)', 'from stdnum import iso11649\niso11649.'+method+'(x)', 'from stdnum.iso11649 import '+method+'\n'+method+'(x)', 'from stdnum.iso11649 import '+method+' as v\nv(x)'])
        for name in GENERIC_NAMES:
            routes.extend(['obj.'+name+'(x)', 'obj = object()\nobj.'+name+'(x)', 'from library import '+name+'\n'+name+'(x)', 'from library import '+name+' as f\nf(x)'])
        for route in routes:
            with self.subTest(route=route):
                self.assertTrue(evidence(route))

    def test_not_evidence(self):
        cases = ['import stdnum.iso11649', 'iso11649(x)', 'validate(x)', 'is_valid(x)', 'compact(x)', 'format(x)', 'validate_rf_creditor_reference(x)', 'obj.validate(x)', 'obj.is_valid(x)', 'import stdnum.iso11649\nstdnum.iso11649.compact(x)', 'import stdnum.iso11649\nstdnum.iso11649.format(x)', 'import stdnum.iso7064.mod_97_10\nstdnum.iso7064.mod_97_10.validate(x)', 'import stdnum.iso7064.mod_97_10\nstdnum.iso7064.mod_97_10.calc_check_digits(x)', 'import stdnum.iban\nstdnum.iban.validate(x)', 'import stdnum.iban\nstdnum.iban.is_valid(x)', 'import stdnum.ean\nstdnum.ean.validate(x)', 'import stdnum.ean\nstdnum.ean.calc_check_digit(x)', 'import stdnum.luhn\nstdnum.luhn.validate(x)', 'import stdnum.luhn\nstdnum.luhn.calc_check_digit(x)', 'import re\nre.match("RF", x)', 'import re\nre.search("RF", x)', 'import re\nre.fullmatch("RF", x)', 'len(x) >= 5', 'x.startswith("RF")', 'registry.lookup(x)', 'validators.iso11649(x)', 'validators.validate_rf_creditor_reference(x)', 'from validators import validate_rf_creditor_reference\nvalidate_rf_creditor_reference(x)', 'idutils.is_iso11649(x)', '"validate rf creditor reference"', '# obj.validate_rf_creditor_reference(x)', 'obj.validate_rf_creditor_reference', 'def broken(:', 'import stdnum.iso11649 as m\nm = None\nm.validate(x)', 'from stdnum.iso11649 import validate\ndef validate(x): pass\nvalidate(x)', 'from lib import validate_rf_creditor_reference as f\nwith open(x) as f: pass\nf(x)', 'import lib as x\nwith open(y) as x: pass\nx.validate_rf_creditor_reference(z)', 'def validate_rf_creditor_reference(x): pass\nobj.validate_rf_creditor_reference(x)', 'import subprocess\nsubprocess.run(["checker", x])']
        for case in cases:
            with self.subTest(case=case):
                self.assertFalse(evidence(case))

    def test_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p/'README.md').write_text('validate iso 11649')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'tests').mkdir()
            (p/'tests/test_x.py').write_text('import stdnum.iso11649\nstdnum.iso11649.validate(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('import stdnum.iso11649')
            (p/'b.py').write_text('stdnum.iso11649.validate(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('import stdnum.iso11649\nstdnum.iso11649.validate(x)')
            self.assertEqual(audit(p), [])
            (p/'README.md').write_text('no iso 11649 validation')
            self.assertEqual(audit(p)[0]['id'], 'documented-no-iso11649-validation-claim-false')
            self.assertEqual(audit(p, ['a.py']), [])
            (p/'a.py').unlink()
            self.assertEqual(audit(p), [])

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p/'README.md').write_text('validate iso 11649')
            (p/'test_x.py').write_text('import stdnum.iso11649\nstdnum.iso11649.validate(x)')
            cmd = [sys.executable, '-m', 'iso11649_validation_claim_audit', 'audit', tmp]
            result = subprocess.run(cmd+['--json'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)['findings'][0]['id'], 'documented-iso11649-validation-claim-false')
            self.assertEqual(subprocess.run(cmd+['--fail-on', 'medium'], capture_output=True).returncode, 2)
            self.assertEqual(subprocess.run(cmd+['--ignore', 'test_x.py'], capture_output=True).returncode, 2)
            self.assertEqual(subprocess.run(cmd+['--fail-on', 'HIGH'], capture_output=True).returncode, 1)
            self.assertEqual(subprocess.run([sys.executable, '-m', 'iso11649_validation_claim_audit', 'audit', tmp+'/missing'], capture_output=True).returncode, 1)

    def test_readme(self):
        text = (ROOT/'README.md').read_text()
        prose = '\n'.join(text.split('```')[::2]).lower()
        for phrase in ISO11649VALIDATION + NOISO11649VALIDATION:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, prose)
        self.assertEqual(claims(text), (False, False))
        self.assertEqual(audit(ROOT), [])
        self.assertNotIn('the phrase', text)
        self.assertNotIn('a tool that', text)
        self.assertEqual(len(ISO11649VALIDATION), 50)
        self.assertEqual(len(NOISO11649VALIDATION), 24)
        self.assertEqual(len(GENERIC_NAMES), 24)
        for value in ('iso11649-validation-claim-audit', 'documented-iso11649-validation-claim-false', 'documented-no-iso11649-validation-claim-false'):
            self.assertEqual(claims(value), (False, False))


if __name__ == '__main__':
    unittest.main()
