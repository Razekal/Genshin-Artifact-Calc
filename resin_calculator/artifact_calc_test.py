import re

import artifact_calc

def test_artifact_init(capsys):
    artifact_calc.initializeArtifact(4, "", "", "", "", "", "", "")
    output = capsys.readouterr().out
    assert re.search("^4", output) is not None
