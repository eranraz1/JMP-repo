from __future__ import division
import jmp_score as jmp
from math import *
import numpy as np


""" ==================================================================
 Copyright(C) 2018 SAS Institute Inc.All rights reserved.
 
 Notice:
 The following permissions are granted provided that the
 above copyright and this notice appear in the score code and
 any related documentation. Permission to copy, modify
 and distribute the score code generated using
 JMP(R) software is limited to customers of SAS Institute Inc. ("SAS")
 and successive third parties, all without any warranty, express or
 implied, or any other obligation by SAS. SAS and all other SAS
 Institute Inc. product and service names are registered
 trademarks or trademarks of SAS Institute Inc. in the USA
 and other countries. Except as contained in this notice,
 the name of the SAS Institute Inc. and JMP shall not be used in
 the advertising or promotion of products or services without
 prior written authorization from SAS Institute Inc.
 ================================================================== """

#set parameters
#indata_aa =  {'DESIGN_LAYERS': 6,'EXISTS_LASER_DRILL' : 'YES' }

def getModelMetadata():
    return {"creator": u"Formula Editor", "modelName": u"", "predicted": u"", "table": u"NEW JMP Pricing 30 RIGID SHORT", "version": u"15.0.0", "timestamp": u"2020-08-30T10:46:03Z"}


def getInputMetadata():
    return {
        u"DESIGN_LAYERS": "float",
        u"EXISTS_LASER_DRILL": "str"

    }


def getOutputMetadata():
    return {
        u"Add": "float"
    }


def score2(indata, outdata):
    _temp_0 = np.nan

    if (indata[u"EXISTS_LASER_DRILL"] == u"NO"):
        _temp_0 = -130.203324304508
    elif (indata[u"EXISTS_LASER_DRILL"] == u"YES"):
        _temp_0 = 130.203324304508
    else:
        _temp_0 = np.nan
        print (_temp_0)
    outdata["Add"] = 20 + 26.8517927560789 * indata[u"DESIGN_LAYERS"] + _temp_0

    return outdata["Add"]



''' GET JSON BACK
dict_result={'Result:': score(param,{})}
print(dict_result)
with open ("result.json","W") as outfile:
    json.dump(dict_result,outfile)
'''


# print('***************************')
# print(getOutputMetadata())
# # https://www.jmp.com/support/help/en/15.2/index.shtml#page/jmp/generating-scoring-code-from-the-formula-depot-platform.shtml
