"""Composition root: wires the core and business layers into pytest.

``pytester`` is only used by the template's self-checks in tests/framework/.
"""

pytest_plugins = ["core.plugin", "business.fixtures", "pytester"]
