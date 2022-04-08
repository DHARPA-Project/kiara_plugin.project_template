# -*- coding: utf-8 -*-
#  Copyright (c) 2022-2022, Markus Binsteiner
#
#  Mozilla Public License, version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)

import builtins
from typing import Dict, Any

from kiara.kiara import Kiara
from kiara.doc.gen_info_pages import generate_detail_pages

pkg_name = "kiara_plugin.{{ cookiecutter.project_slug }}"
kiara: Kiara = Kiara.instance()

data_types = kiara.type_registry.get_context_metadata(only_for_package=pkg_name)
modules = kiara.module_registry.get_context_metadata(only_for_package=pkg_name)

operation_types = kiara.operation_registry.get_context_metadata(only_for_package=pkg_name)

types: Dict[str, Dict[str, Any]] = {}
if data_types:
    types["data_types"] = data_types
if modules:
    types["modules"] = modules
if operation_types:
    types["operation_types"] = operation_types


generate_detail_pages(
    type_item_details=types,
)

builtins.plugin_package_context_info = types

