# -*- coding: utf-8 -*-
# %%
from typing import List

# %%
DEBUG = False

RECIPIANT_LISTS = {
    "shift_supervisors": [
        "supervisor_A@company.com",
        "supervisor_B@company.com",
        "supervisor_C@company.com",
        "supervisor_D@company.com",
        "supervisor_E@company.com",
    ],
    "include_area_managers": [
        "supervisor_A@company.com",
        "supervisor_B@company.com",
        "supervisor_C@company.com",
        "supervisor_D@company.com",
        "supervisor_E@company.com",
        "manager_A@company.com",
        "manager_B@company.com",
        "manager_C@company.com",
        "manager_D@company.com",
        "manager_E@company.com",
    ],
}

# %%
def get_recipiant_list(which: str = "shift_supervisors") -> List[str]:
    """Get a recipiant list for emails."""
    if DEBUG:
        recip_list = ["user@company.com"]
    else:
        recip_list = RECIPIANT_LISTS[which]

    return recip_list


# %%
