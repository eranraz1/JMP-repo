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

""" Python code generated by JMP v15.0.0 """

def getModelMetadata():
	return {"creator": u"Formula Editor", "modelName": u"", "predicted": u"", "table": u"Subset of JMP 31.12.2020 PRICE  Rigid Flex Final", "version": u"15.0.0", "timestamp": u"2021-01-04T12:54:15Z"}


def getInputMetadata():
    return {
        u"AUSSS": "float",
        u"BOARD_TYPE": "str",
        u"CAM_PNL_SIZE_X": "float",
        u"CAM_PNL_SIZE_Y": "float",
        u"COCOON_DEPT_ROUT": "str",
        u"EXIST_LASER": "str",
        u"FAI_TYPE": "str",
        u"FINISH_CS": "str",
        u"FINISH_THK": "float",
        u"FLEX_CLADS_NUM": "float",
        u"HATS_COUPON_TYPE": "str",
        u"JOB_SUB_NUM": "float",
        u"NUM_DESIGN_LAYERS": "float",
        u"NUM_PCBS_PNL": "float",
        u"PASTE_TYPE": "str",
        u"STRAIN_RELIEF": "str",
        u"WRAP_REQUIRMENT": "str"
	}


def getOutputMetadata():
    return {
        u"Add": "float"
	}


def score(indata, outdata):
    # WRAP_REQUIRMENT_asCode
    # STRAIN_RELIEF_asCode
    # PASTE_TYPE_asCode
    # HATS_COUPON_TYPE_asCode
    # FINISH_CS_asCode
    # FAI_TYPE_asCode
    # EXIST_LASER_asCode
    # COCOON_DEPT_ROUT_asCode
    # BOARD_TYPE_asCode
    _temp_0 = np.nan
    _temp_1 = np.nan
    _temp_2 = np.nan
    _temp_3 = np.nan
    _temp_4 = np.nan
    _temp_5 = np.nan
    _temp_6 = np.nan
    _temp_7 = np.nan
    _temp_8 = np.nan
    _temp_9 = np.nan
    _temp_10 = np.nan
    _temp_11 = np.nan
    _temp_12 = np.nan
    _temp_13 = np.nan
    _temp_14 = np.nan
    _temp_15 = np.nan
    _temp_16 = np.nan
    _temp_17 = np.nan
    _temp_18 = np.nan
    _temp_19 = np.nan
    _temp_20 = np.nan
    _temp_21 = np.nan
    _temp_22 = np.nan
    _temp_23 = np.nan
    _temp_24 = np.nan
    _temp_25 = np.nan
    _temp_26 = np.nan
    _temp_27 = np.nan
    _temp_28 = np.nan
    _temp_29 = np.nan
    _temp_30 = np.nan
    _temp_31 = np.nan
    _temp_32 = np.nan
    _temp_33 = np.nan
    _temp_34 = np.nan
    _temp_35 = np.nan
    _temp_36 = np.nan
    _temp_37 = np.nan
    _temp_38 = np.nan
    _temp_39 = np.nan
    _temp_40 = np.nan
    _temp_41 = np.nan
    _temp_42 = np.nan
    _temp_43 = np.nan
    _temp_44 = np.nan
    _temp_45 = np.nan
    _temp_46 = np.nan
    _temp_47 = np.nan
    _temp_48 = np.nan
    _temp_49 = np.nan
    _temp_50 = np.nan
    _temp_51 = np.nan
    _temp_52 = np.nan
    _temp_53 = np.nan
    _temp_54 = np.nan
    _temp_55 = np.nan
    _temp_56 = np.nan
    _temp_57 = np.nan
    _temp_58 = np.nan
    _temp_59 = np.nan
    _temp_60 = np.nan
    _temp_61 = np.nan
    _temp_62 = np.nan
    _temp_63 = np.nan
    _temp_64 = np.nan
    _temp_65 = np.nan
    _temp_66 = np.nan
    _temp_67 = np.nan
    _temp_68 = np.nan
    _temp_69 = np.nan
    _temp_70 = np.nan
    _temp_71 = np.nan
    _temp_72 = np.nan
    _temp_73 = np.nan
    _temp_74 = np.nan
    _temp_75 = np.nan
    _temp_76 = np.nan
    _temp_77 = np.nan
    _temp_78 = np.nan
    _temp_79 = np.nan
    _temp_80 = np.nan
    _temp_81 = np.nan
    _temp_82 = np.nan
    _temp_83 = np.nan

    if (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS2"):
        _temp_0 = 0
    elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS3"):
        _temp_0 = 1
    elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6012 CLASS2"):
        _temp_0 = 2
    elif (indata[u"WRAP_REQUIRMENT"] == u"NONE"):
        _temp_0 = 3
    WRAP_REQUIRMENT_asCode = _temp_0

    if (indata[u"STRAIN_RELIEF"] == u"NO"):
        _temp_1 = 0
    elif (indata[u"STRAIN_RELIEF"] == u"YES"):
        _temp_1 = 1
    STRAIN_RELIEF_asCode = _temp_1

    if (indata[u"PASTE_TYPE"] == u"NONE"):
        _temp_2 = 0
    elif (indata[u"PASTE_TYPE"] == u"THROUGH"):
        _temp_2 = 1
    elif (indata[u"PASTE_TYPE"] == u"LASER"):
        _temp_2 = 2
    elif (indata[u"PASTE_TYPE"] == u"LASER-THROUGH"):
        _temp_2 = 3
    elif (indata[u"PASTE_TYPE"] == u"THROUGH-LASER BACK DRILL"):
        _temp_2 = 4
    PASTE_TYPE_asCode = _temp_2

    if (indata[u"HATS_COUPON_TYPE"] == u"INTERNAL"):
        _temp_3 = 0
    elif (indata[u"HATS_COUPON_TYPE"] == u"EXTERNAL"):
        _temp_3 = 1
    elif (indata[u"HATS_COUPON_TYPE"] == u"NONE"):
        _temp_3 = 2
    HATS_COUPON_TYPE_asCode = _temp_3

    if (indata[u"FINISH_CS"] == u"HAL"):
        _temp_4 = 0
    elif (indata[u"FINISH_CS"] == u"CHM_GOLD"):
        _temp_4 = 1
    elif (indata[u"FINISH_CS"] == u"ENEPIG"):
        _temp_4 = 2
    elif (indata[u"FINISH_CS"] == u"CHM_TIN"):
        _temp_4 = 3
    elif (indata[u"FINISH_CS"] == u"NONE"):
        _temp_4 = 4
    FINISH_CS_asCode = _temp_4

    if (indata[u"FAI_TYPE"] == u"NONE"):
        _temp_5 = 0
    elif (indata[u"FAI_TYPE"] == u"PER AS9100 MICRO SECTION"):
        _temp_5 = 1
    elif (indata[u"FAI_TYPE"] == u"PER AS9102 REPORT"):
        _temp_5 = 2
    elif (indata[u"FAI_TYPE"] == u"RC-06"):
        _temp_5 = 3
    elif (indata[u"FAI_TYPE"] == u"RC-28"):
        _temp_5 = 4
    FAI_TYPE_asCode = _temp_5

    if (indata[u"EXIST_LASER"] == u"NO"):
        _temp_6 = 0
    elif (indata[u"EXIST_LASER"] == u"YES"):
        _temp_6 = 1
    EXIST_LASER_asCode = _temp_6

    if (indata[u"COCOON_DEPT_ROUT"] == u"NO"):
        _temp_7 = 0
    elif (indata[u"COCOON_DEPT_ROUT"] == u"YES"):
        _temp_7 = 1
    COCOON_DEPT_ROUT_asCode = _temp_7

    if (indata[u"BOARD_TYPE"] == u"GENERAL"):
        _temp_8 = 0
    elif (indata[u"BOARD_TYPE"] == u"MILITARY"):
        _temp_8 = 1
    elif (indata[u"BOARD_TYPE"] == u"COMMERCIAL"):
        _temp_8 = 2
    BOARD_TYPE_asCode = _temp_8

    if (jmp.numeq(BOARD_TYPE_asCode, 0)):
        _temp_9 = 1
    elif (jmp.numeq(BOARD_TYPE_asCode, 1)):
        _temp_9 = -1
    elif (jmp.numeq(BOARD_TYPE_asCode, 2)):
        _temp_9 = -1
    else:
        _temp_9 = np.nan
    if (jmp.numeq(BOARD_TYPE_asCode, 1)):
        _temp_10 = 1
    elif (jmp.numeq(BOARD_TYPE_asCode, 2)):
        _temp_10 = -1
    else:
        _temp_10 = 0
    if (jmp.numeq(COCOON_DEPT_ROUT_asCode, 0)):
        _temp_11 = -187.78029576242
    elif (jmp.numeq(COCOON_DEPT_ROUT_asCode, 1)):
        _temp_11 = 187.78029576242
    else:
        _temp_11 = np.nan
    if (jmp.numeq(COCOON_DEPT_ROUT_asCode, 0)):
        _temp_12 = -167.43774582174
    elif (jmp.numeq(COCOON_DEPT_ROUT_asCode, 1)):
        _temp_12 = 167.43774582174
    else:
        _temp_12 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_13 = -1166.43313817189
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_13 = 1166.43313817189
    else:
        _temp_13 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_14 = -844.373481076387
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_14 = 844.373481076387
    else:
        _temp_14 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_15 = 1450.60070359118
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_15 = -1450.60070359118
    else:
        _temp_15 = np.nan
    if (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_16 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_16 = -1
    else:
        _temp_16 = 0
    if (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_17 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_17 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 2)):
        _temp_17 = -1
    else:
        _temp_17 = 0
    if (jmp.numeq(FAI_TYPE_asCode, 3)):
        _temp_18 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 4)):
        _temp_18 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_18 = -1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_18 = -1
    elif (jmp.numeq(FAI_TYPE_asCode, 2)):
        _temp_18 = -1
    else:
        _temp_18 = np.nan
    if (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_19 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_19 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_19 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_19 = -1
    else:
        _temp_19 = 0
    if (jmp.numeq(FINISH_CS_asCode, 4)):
        _temp_20 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_20 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_20 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_20 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_20 = -1
    else:
        _temp_20 = np.nan
    if (jmp.numeq(HATS_COUPON_TYPE_asCode, 0)):
        _temp_21 = 1
    elif (jmp.numeq(HATS_COUPON_TYPE_asCode, 1)):
        _temp_21 = -1
    else:
        _temp_21 = 0
    if (jmp.numeq(HATS_COUPON_TYPE_asCode, 2)):
        _temp_22 = 1
    elif (jmp.numeq(HATS_COUPON_TYPE_asCode, 0)):
        _temp_22 = -1
    elif (jmp.numeq(HATS_COUPON_TYPE_asCode, 1)):
        _temp_22 = -1
    else:
        _temp_22 = np.nan
    if (jmp.numeq(PASTE_TYPE_asCode, 0)):
        _temp_23 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 1)):
        _temp_23 = -1
    elif (jmp.numeq(PASTE_TYPE_asCode, 2)):
        _temp_23 = -1
    else:
        _temp_23 = 0
    if (jmp.numeq(PASTE_TYPE_asCode, 0)):
        _temp_24 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 1)):
        _temp_24 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 2)):
        _temp_24 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 3)):
        _temp_24 = -1
    elif (jmp.numeq(PASTE_TYPE_asCode, 4)):
        _temp_24 = -1
    else:
        _temp_24 = np.nan
    if (jmp.numeq(PASTE_TYPE_asCode, 1)):
        _temp_25 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 2)):
        _temp_25 = -1
    else:
        _temp_25 = 0
    if (jmp.numeq(WRAP_REQUIRMENT_asCode, 0)):
        _temp_26 = 1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 1)):
        _temp_26 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 2)):
        _temp_26 = -1
    else:
        _temp_26 = 0
    if (jmp.numeq(WRAP_REQUIRMENT_asCode, 3)):
        _temp_27 = 1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 0)):
        _temp_27 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 1)):
        _temp_27 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 2)):
        _temp_27 = -1
    else:
        _temp_27 = np.nan
    if (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_28 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_28 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_28 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_28 = -1
    else:
        _temp_28 = 0
    if (jmp.numeq(WRAP_REQUIRMENT_asCode, 0)):
        _temp_29 = 1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 1)):
        _temp_29 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 2)):
        _temp_29 = -1
    else:
        _temp_29 = 0
    if (jmp.numeq(BOARD_TYPE_asCode, 1)):
        _temp_30 = 1
    elif (jmp.numeq(BOARD_TYPE_asCode, 2)):
        _temp_30 = -1
    else:
        _temp_30 = 0
    if (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_31 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_31 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 2)):
        _temp_31 = -1
    else:
        _temp_31 = 0
    if (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_32 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_32 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_32 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_32 = -1
    else:
        _temp_32 = 0
    if (jmp.numeq(WRAP_REQUIRMENT_asCode, 0)):
        _temp_33 = 1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 1)):
        _temp_33 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 2)):
        _temp_33 = -1
    else:
        _temp_33 = 0
    if (jmp.numeq(BOARD_TYPE_asCode, 1)):
        _temp_34 = 1
    elif (jmp.numeq(BOARD_TYPE_asCode, 2)):
        _temp_34 = -1
    else:
        _temp_34 = 0
    if (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_35 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_35 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 2)):
        _temp_35 = -1
    else:
        _temp_35 = 0
    if (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_36 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_36 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_36 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_36 = -1
    else:
        _temp_36 = 0
    if (jmp.numeq(WRAP_REQUIRMENT_asCode, 0)):
        _temp_37 = 1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 1)):
        _temp_37 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 2)):
        _temp_37 = -1
    else:
        _temp_37 = 0
    if (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_38 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_38 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_38 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_38 = -1
    else:
        _temp_38 = 0
    if (jmp.numeq(PASTE_TYPE_asCode, 0)):
        _temp_39 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 1)):
        _temp_39 = -1
    elif (jmp.numeq(PASTE_TYPE_asCode, 2)):
        _temp_39 = -1
    else:
        _temp_39 = 0
    if (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_40 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_40 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_40 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_40 = -1
    else:
        _temp_40 = 0
    if (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_41 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_41 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_41 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_41 = -1
    else:
        _temp_41 = 0
    if (jmp.numeq(BOARD_TYPE_asCode, 1)):
        _temp_42 = 1
    elif (jmp.numeq(BOARD_TYPE_asCode, 2)):
        _temp_42 = -1
    else:
        _temp_42 = 0
    if (jmp.numeq(COCOON_DEPT_ROUT_asCode, 0)):
        _temp_43 = -167.43774582174
    elif (jmp.numeq(COCOON_DEPT_ROUT_asCode, 1)):
        _temp_43 = 167.43774582174
    else:
        _temp_43 = np.nan
    if (jmp.numeq(BOARD_TYPE_asCode, 1)):
        _temp_44 = 1
    elif (jmp.numeq(BOARD_TYPE_asCode, 2)):
        _temp_44 = -1
    else:
        _temp_44 = 0
    if (jmp.numeq(WRAP_REQUIRMENT_asCode, 3)):
        _temp_45 = 1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 0)):
        _temp_45 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 1)):
        _temp_45 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 2)):
        _temp_45 = -1
    else:
        _temp_45 = np.nan
    if (jmp.numeq(COCOON_DEPT_ROUT_asCode, 0)):
        _temp_46 = -187.78029576242
    elif (jmp.numeq(COCOON_DEPT_ROUT_asCode, 1)):
        _temp_46 = 187.78029576242
    else:
        _temp_46 = np.nan
    if (jmp.numeq(FINISH_CS_asCode, 0)):
        _temp_47 = 1
    elif (jmp.numeq(FINISH_CS_asCode, 1)):
        _temp_47 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 2)):
        _temp_47 = -1
    elif (jmp.numeq(FINISH_CS_asCode, 3)):
        _temp_47 = -1
    else:
        _temp_47 = 0
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_48 = -1166.43313817189
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_48 = 1166.43313817189
    else:
        _temp_48 = np.nan
    if (jmp.numeq(FAI_TYPE_asCode, 3)):
        _temp_49 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 4)):
        _temp_49 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_49 = -1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_49 = -1
    elif (jmp.numeq(FAI_TYPE_asCode, 2)):
        _temp_49 = -1
    else:
        _temp_49 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_50 = -844.373481076387
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_50 = 844.373481076387
    else:
        _temp_50 = np.nan
    if (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_51 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_51 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 2)):
        _temp_51 = -1
    else:
        _temp_51 = 0
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_52 = 1450.60070359118
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_52 = -1450.60070359118
    else:
        _temp_52 = np.nan
    if (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_53 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_53 = -1
    else:
        _temp_53 = 0
    if (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_54 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_54 = -1
    else:
        _temp_54 = 0
    if (jmp.numeq(PASTE_TYPE_asCode, 0)):
        _temp_55 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 1)):
        _temp_55 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 2)):
        _temp_55 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 3)):
        _temp_55 = -1
    elif (jmp.numeq(PASTE_TYPE_asCode, 4)):
        _temp_55 = -1
    else:
        _temp_55 = np.nan
    if (jmp.numeq(FAI_TYPE_asCode, 0)):
        _temp_56 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 1)):
        _temp_56 = 1
    elif (jmp.numeq(FAI_TYPE_asCode, 2)):
        _temp_56 = -1
    else:
        _temp_56 = 0
    if (jmp.numeq(HATS_COUPON_TYPE_asCode, 2)):
        _temp_57 = 1
    elif (jmp.numeq(HATS_COUPON_TYPE_asCode, 0)):
        _temp_57 = -1
    elif (jmp.numeq(HATS_COUPON_TYPE_asCode, 1)):
        _temp_57 = -1
    else:
        _temp_57 = np.nan
    if (jmp.numeq(PASTE_TYPE_asCode, 0)):
        _temp_58 = 1
    elif (jmp.numeq(PASTE_TYPE_asCode, 1)):
        _temp_58 = -1
    elif (jmp.numeq(PASTE_TYPE_asCode, 2)):
        _temp_58 = -1
    else:
        _temp_58 = 0
    if (jmp.numeq(WRAP_REQUIRMENT_asCode, 3)):
        _temp_59 = 1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 0)):
        _temp_59 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 1)):
        _temp_59 = -1
    elif (jmp.numeq(WRAP_REQUIRMENT_asCode, 2)):
        _temp_59 = -1
    else:
        _temp_59 = np.nan
    if (jmp.numeq(COCOON_DEPT_ROUT_asCode, 0)):
        _temp_60 = 880.968392152077
    elif (jmp.numeq(COCOON_DEPT_ROUT_asCode, 1)):
        _temp_60 = -880.968392152077
    else:
        _temp_60 = np.nan
    if (jmp.numeq(COCOON_DEPT_ROUT_asCode, 0)):
        _temp_61 = -8739.8440919569 + 509.436834260786 * indata[u"CAM_PNL_SIZE_X"]
    elif (jmp.numeq(COCOON_DEPT_ROUT_asCode, 1)):
        _temp_61 = 8739.8440919569 + -509.436834260786 * indata[u"CAM_PNL_SIZE_X"]
    else:
        _temp_61 = np.nan
    if (jmp.numeq(COCOON_DEPT_ROUT_asCode, 0)):
        _temp_62 = 11625.5461554537 + -501.068279069865 * indata[u"CAM_PNL_SIZE_Y"]
    elif (jmp.numeq(COCOON_DEPT_ROUT_asCode, 1)):
        _temp_62 = -11625.5461554537 + 501.068279069865 * indata[u"CAM_PNL_SIZE_Y"]
    else:
        _temp_62 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_63 = 1186.3789040392
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_63 = -1186.3789040392
    else:
        _temp_63 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_64 = -2468.87791549747 + 143.083933842185 * indata[u"AUSSS"]
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_64 = 2468.87791549747 + -143.083933842185 * indata[u"AUSSS"]
    else:
        _temp_64 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        if (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS2"):
            _temp_66 = 1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS3"):
            _temp_66 = -1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6012 CLASS2"):
            _temp_66 = -1
        else:
            _temp_66 = 0
        _temp_65 = 7.13582111271729 + 625.573650881549 * _temp_66
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        if (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS2"):
            _temp_67 = 1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS3"):
            _temp_67 = -1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6012 CLASS2"):
            _temp_67 = -1
        else:
            _temp_67 = 0
        _temp_65 = -7.13582111271729 + -625.573650881549 * _temp_67
    else:
        _temp_65 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        _temp_68 = 4339.83123201663 + -512.747355804301 * indata[u"NUM_DESIGN_LAYERS"]
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        _temp_68 = -4339.83123201663 + 512.747355804301 * indata[u"NUM_DESIGN_LAYERS"]
    else:
        _temp_68 = np.nan
    if (jmp.numeq(EXIST_LASER_asCode, 0)):
        if (indata[u"COCOON_DEPT_ROUT"] == u"NO"):
            _temp_70 = -760.826610081856
        elif (indata[u"COCOON_DEPT_ROUT"] == u"YES"):
            _temp_70 = 760.826610081856
        else:
            _temp_70 = np.nan
        _temp_69 = _temp_70
    elif (jmp.numeq(EXIST_LASER_asCode, 1)):
        if (indata[u"COCOON_DEPT_ROUT"] == u"NO"):
            _temp_71 = 760.826610081856
        elif (indata[u"COCOON_DEPT_ROUT"] == u"YES"):
            _temp_71 = -760.826610081856
        else:
            _temp_71 = np.nan
        _temp_69 = _temp_71
    else:
        _temp_69 = np.nan
    if (jmp.numeq(STRAIN_RELIEF_asCode, 0)):
        _temp_72 = 95.9369002476591
    elif (jmp.numeq(STRAIN_RELIEF_asCode, 1)):
        _temp_72 = -95.9369002476591
    else:
        _temp_72 = np.nan
    if (jmp.numeq(STRAIN_RELIEF_asCode, 0)):
        _temp_73 = -2275.22241530628 + 98.0635029868162 * indata[u"CAM_PNL_SIZE_Y"]
    elif (jmp.numeq(STRAIN_RELIEF_asCode, 1)):
        _temp_73 = 2275.22241530628 + -98.0635029868162 * indata[u"CAM_PNL_SIZE_Y"]
    else:
        _temp_73 = np.nan
    if (jmp.numeq(STRAIN_RELIEF_asCode, 0)):
        if (indata[u"PASTE_TYPE"] == u"NONE"):
            _temp_75 = 1
        elif (indata[u"PASTE_TYPE"] == u"THROUGH"):
            _temp_75 = -1
        elif (indata[u"PASTE_TYPE"] == u"LASER"):
            _temp_75 = -1
        else:
            _temp_75 = 0
        _temp_74 = -402.220626688379 + 874.248139000362 * _temp_75
    elif (jmp.numeq(STRAIN_RELIEF_asCode, 1)):
        if (indata[u"PASTE_TYPE"] == u"NONE"):
            _temp_76 = 1
        elif (indata[u"PASTE_TYPE"] == u"THROUGH"):
            _temp_76 = -1
        elif (indata[u"PASTE_TYPE"] == u"LASER"):
            _temp_76 = -1
        else:
            _temp_76 = 0
        _temp_74 = 402.220626688379 + -874.248139000362 * _temp_76
    else:
        _temp_74 = np.nan
    if (jmp.numeq(STRAIN_RELIEF_asCode, 0)):
        _temp_77 = -235.40127283011 + 1289.80280738165 * indata[u"JOB_SUB_NUM"]
    elif (jmp.numeq(STRAIN_RELIEF_asCode, 1)):
        _temp_77 = 235.40127283011 + -1289.80280738165 * indata[u"JOB_SUB_NUM"]
    else:
        _temp_77 = np.nan
    if (jmp.numeq(STRAIN_RELIEF_asCode, 0)):
        if (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS2"):
            _temp_79 = 1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS3"):
            _temp_79 = -1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6012 CLASS2"):
            _temp_79 = -1
        else:
            _temp_79 = 0
        _temp_78 = 11.4727510391415 + 1005.77784109807 * _temp_79
    elif (jmp.numeq(STRAIN_RELIEF_asCode, 1)):
        if (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS2"):
            _temp_80 = 1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS3"):
            _temp_80 = -1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6012 CLASS2"):
            _temp_80 = -1
        else:
            _temp_80 = 0
        _temp_78 = -11.4727510391415 + -1005.77784109807 * _temp_80
    else:
        _temp_78 = np.nan
    if (jmp.numeq(STRAIN_RELIEF_asCode, 0)):
        if (indata[u"WRAP_REQUIRMENT"] == u"NONE"):
            _temp_82 = 1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS2"):
            _temp_82 = -1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS3"):
            _temp_82 = -1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6012 CLASS2"):
            _temp_82 = -1
        else:
            _temp_82 = np.nan
        _temp_81 = 141.983460535943 + -829.814447132292 * _temp_82
    elif (jmp.numeq(STRAIN_RELIEF_asCode, 1)):
        if (indata[u"WRAP_REQUIRMENT"] == u"NONE"):
            _temp_83 = 1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS2"):
            _temp_83 = -1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6013 CLASS3"):
            _temp_83 = -1
        elif (indata[u"WRAP_REQUIRMENT"] == u"IPC 6012 CLASS2"):
            _temp_83 = -1
        else:
            _temp_83 = np.nan
        _temp_81 = -141.983460535943 + 829.814447132292 * _temp_83
    else:
        _temp_81 = np.nan
    outdata[u"Add"] = 293.029629308197 + -40.9173578555378 * indata[u"AUSSS"] + 178.131214420167 * indata[u"CAM_PNL_SIZE_X"] + -202.538542076484 * indata[u"CAM_PNL_SIZE_Y"] + -3418.49059699426 * indata[u"FINISH_THK"] + 304.237584882385 * indata[u"FLEX_CLADS_NUM"] + 392.254040714125 * indata[u"JOB_SUB_NUM"] + 637.42914939802 * indata[u"NUM_DESIGN_LAYERS"] + 25.6075725585235 * indata[u"NUM_PCBS_PNL"] + -296.704824675502 * _temp_9 + -926.553850474232 * _temp_10 + 0.44106463878327 * _temp_11 + -0.711026615969582 * _temp_12 + 0.870722433460076 * _temp_13 + 0.0304182509505703 * _temp_14 + -0.247148288973384 * _temp_15 + 338.333983099763 * _temp_16 + 4323.70657394805 * _temp_17 + 1018.35033444079 * _temp_18 + -3257.77224722335 * _temp_19 + 333.440577215135 * _temp_20 + -1010.19432306386 * _temp_21 + 193.109107645822 * _temp_22 + 316.497117767196 * _temp_23 + 894.304551980516 * _temp_24 + -3151.41344969722 * _temp_25 + -4192.95331374068 * _temp_26 + -861.995740929363 * _temp_27 + -56.1830683334781 * indata[u"AUSSS"] * indata[u"FINISH_THK"] + 17.4411358149239 * indata[u"AUSSS"] * indata[u"FLEX_CLADS_NUM"] + -33.1997184647022 * indata[u"AUSSS"] * _temp_28 + -39.0913132672548 * indata[u"AUSSS"] * _temp_29 + -443.515445778742 * indata[u"CAM_PNL_SIZE_X"] * _temp_30 + 238.060196651545 * indata[u"CAM_PNL_SIZE_X"] * _temp_31 + -606.673873879321 * indata[u"CAM_PNL_SIZE_X"] * _temp_32 + -891.245514415937 * indata[u"CAM_PNL_SIZE_X"] * _temp_33 + 200.991469143205 * indata[u"CAM_PNL_SIZE_Y"] * indata[u"FINISH_THK"] + 367.4141115339 * indata[u"CAM_PNL_SIZE_Y"] * _temp_34 + -300.204080452811 * indata[u"CAM_PNL_SIZE_Y"] * _temp_35 + 623.723564081878 * indata[u"CAM_PNL_SIZE_Y"] * _temp_36 + 894.559924753848 * indata[u"CAM_PNL_SIZE_Y"] * _temp_37 + 4564.3915159023 * indata[u"FINISH_THK"] * indata[u"JOB_SUB_NUM"] + -497.15144510119 * indata[u"FINISH_THK"] * _temp_38 + -776.072224776282 * indata[u"FINISH_THK"] * _temp_39 + -1024.94227296851 * indata[u"FLEX_CLADS_NUM"] * indata[u"JOB_SUB_NUM"] + -478.29695894109 * indata[u"JOB_SUB_NUM"] * indata[u"NUM_DESIGN_LAYERS"] + 636.201692515418 * indata[u"JOB_SUB_NUM"] * _temp_40 + 52.4890839609745 * indata[u"NUM_DESIGN_LAYERS"] * _temp_41 + _temp_42 * _temp_43 + 221.089681177163 * _temp_44 * _temp_45 + _temp_46 * _temp_47 + _temp_48 * _temp_49 + _temp_50 * _temp_51 + _temp_52 * _temp_53 + -2027.77990777937 * _temp_54 * _temp_55 + -593.150166790695 * _temp_56 * _temp_57 + -265.178301248576 * _temp_58 * _temp_59 + _temp_60 + _temp_61 + _temp_62 + _temp_63 + _temp_64 + _temp_65 + _temp_68 + _temp_69 + _temp_72 + _temp_73 + _temp_74 + _temp_77 + _temp_78 + _temp_81

    return outdata[u"Add"]


