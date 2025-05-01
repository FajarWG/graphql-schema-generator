import graphene

class buzzer(graphene.ObjectType):
    id = graphene.ID()
    node = graphene.String()
    BEC = graphene.Float()
    EVC = graphene.Float()
    BEC_Norm = graphene.Float()
    EVC_Norm = graphene.Int()
    final_measure = graphene.Float()
    tweet_url = graphene.String()
    projectId = graphene.String()

class nodesType(graphene.ObjectType):
    nodesType_0 = graphene.Field('nodesType_0')
    nodesType_1 = graphene.Field('nodesType_1')
    nodesType_2 = graphene.Field('nodesType_2')
    nodesType_3 = graphene.Field('nodesType_3')
    nodesType_4 = graphene.Field('nodesType_4')
    nodesType_5 = graphene.Field('nodesType_5')
    nodesType_6 = graphene.Field('nodesType_6')
    nodesType_7 = graphene.Field('nodesType_7')
    nodesType_8 = graphene.Field('nodesType_8')
    nodesType_9 = graphene.Field('nodesType_9')
    nodesType_10 = graphene.Field('nodesType_10')
    nodesType_11 = graphene.Field('nodesType_11')
    nodesType_12 = graphene.Field('nodesType_12')
    nodesType_13 = graphene.Field('nodesType_13')
    nodesType_14 = graphene.Field('nodesType_14')
    nodesType_15 = graphene.Field('nodesType_15')
    nodesType_16 = graphene.Field('nodesType_16')
    nodesType_17 = graphene.Field('nodesType_17')
    nodesType_18 = graphene.Field('nodesType_18')
    nodesType_19 = graphene.Field('nodesType_19')
    nodesType_20 = graphene.Field('nodesType_20')
    nodesType_21 = graphene.Field('nodesType_21')
    nodesType_22 = graphene.Field('nodesType_22')
    nodesType_23 = graphene.Field('nodesType_23')
    nodesType_24 = graphene.Field('nodesType_24')
    nodesType_25 = graphene.Field('nodesType_25')
    nodesType_26 = graphene.Field('nodesType_26')
    nodesType_27 = graphene.Field('nodesType_27')
    nodesType_28 = graphene.Field('nodesType_28')
    nodesType_29 = graphene.Field('nodesType_29')
    nodesType_30 = graphene.Field('nodesType_30')
    nodesType_31 = graphene.Field('nodesType_31')
    nodesType_32 = graphene.Field('nodesType_32')
    nodesType_33 = graphene.Field('nodesType_33')
    nodesType_34 = graphene.Field('nodesType_34')
    nodesType_35 = graphene.Field('nodesType_35')
    nodesType_36 = graphene.Field('nodesType_36')
    nodesType_37 = graphene.Field('nodesType_37')
    nodesType_38 = graphene.Field('nodesType_38')
    nodesType_39 = graphene.Field('nodesType_39')
    nodesType_40 = graphene.Field('nodesType_40')
    nodesType_41 = graphene.Field('nodesType_41')
    nodesType_42 = graphene.Field('nodesType_42')
    nodesType_43 = graphene.Field('nodesType_43')
    nodesType_44 = graphene.Field('nodesType_44')
    nodesType_45 = graphene.Field('nodesType_45')
    nodesType_46 = graphene.Field('nodesType_46')
    nodesType_47 = graphene.Field('nodesType_47')
    nodesType_48 = graphene.Field('nodesType_48')
    nodesType_49 = graphene.Field('nodesType_49')
    nodesType_50 = graphene.Field('nodesType_50')
    nodesType_51 = graphene.Field('nodesType_51')
    nodesType_52 = graphene.Field('nodesType_52')
    nodesType_53 = graphene.Field('nodesType_53')

class nodesType_0(graphene.ObjectType):
    nodesType_0_id = graphene.String()
    nodesType_0_name = graphene.String()
    nodesType_0_val = graphene.Int()
    nodesType_0_community = graphene.Int()
    nodesType_0_profile_url = graphene.String()

class nodesType_1(graphene.ObjectType):
    nodesType_1_id = graphene.String()
    nodesType_1_name = graphene.String()
    nodesType_1_val = graphene.Int()
    nodesType_1_community = graphene.Int()
    nodesType_1_profile_url = graphene.String()

class nodesType_2(graphene.ObjectType):
    nodesType_2_id = graphene.String()
    nodesType_2_name = graphene.String()
    nodesType_2_val = graphene.Int()
    nodesType_2_community = graphene.Int()
    nodesType_2_profile_url = graphene.String()

class nodesType_3(graphene.ObjectType):
    nodesType_3_id = graphene.String()
    nodesType_3_name = graphene.String()
    nodesType_3_val = graphene.Int()
    nodesType_3_community = graphene.Int()
    nodesType_3_profile_url = graphene.String()

class nodesType_4(graphene.ObjectType):
    nodesType_4_id = graphene.String()
    nodesType_4_name = graphene.String()
    nodesType_4_val = graphene.Int()
    nodesType_4_community = graphene.Int()
    nodesType_4_profile_url = graphene.String()

class nodesType_5(graphene.ObjectType):
    nodesType_5_id = graphene.String()
    nodesType_5_name = graphene.String()
    nodesType_5_val = graphene.Int()
    nodesType_5_community = graphene.Int()
    nodesType_5_profile_url = graphene.String()

class nodesType_6(graphene.ObjectType):
    nodesType_6_id = graphene.String()
    nodesType_6_name = graphene.String()
    nodesType_6_val = graphene.Int()
    nodesType_6_community = graphene.Int()
    nodesType_6_profile_url = graphene.String()

class nodesType_7(graphene.ObjectType):
    nodesType_7_id = graphene.String()
    nodesType_7_name = graphene.String()
    nodesType_7_val = graphene.Int()
    nodesType_7_community = graphene.Int()
    nodesType_7_profile_url = graphene.String()

class nodesType_8(graphene.ObjectType):
    nodesType_8_id = graphene.String()
    nodesType_8_name = graphene.String()
    nodesType_8_val = graphene.Int()
    nodesType_8_community = graphene.Int()
    nodesType_8_profile_url = graphene.String()

class nodesType_9(graphene.ObjectType):
    nodesType_9_id = graphene.String()
    nodesType_9_name = graphene.String()
    nodesType_9_val = graphene.Int()
    nodesType_9_community = graphene.Int()
    nodesType_9_profile_url = graphene.String()

class nodesType_10(graphene.ObjectType):
    nodesType_10_id = graphene.String()
    nodesType_10_name = graphene.String()
    nodesType_10_val = graphene.Int()
    nodesType_10_community = graphene.Int()
    nodesType_10_profile_url = graphene.String()

class nodesType_11(graphene.ObjectType):
    nodesType_11_id = graphene.String()
    nodesType_11_name = graphene.String()
    nodesType_11_val = graphene.Int()
    nodesType_11_community = graphene.Int()
    nodesType_11_profile_url = graphene.String()

class nodesType_12(graphene.ObjectType):
    nodesType_12_id = graphene.String()
    nodesType_12_name = graphene.String()
    nodesType_12_val = graphene.Int()
    nodesType_12_community = graphene.Int()
    nodesType_12_profile_url = graphene.String()

class nodesType_13(graphene.ObjectType):
    nodesType_13_id = graphene.String()
    nodesType_13_name = graphene.String()
    nodesType_13_val = graphene.Int()
    nodesType_13_community = graphene.Int()
    nodesType_13_profile_url = graphene.String()

class nodesType_14(graphene.ObjectType):
    nodesType_14_id = graphene.String()
    nodesType_14_name = graphene.String()
    nodesType_14_val = graphene.Int()
    nodesType_14_community = graphene.Int()
    nodesType_14_profile_url = graphene.String()

class nodesType_15(graphene.ObjectType):
    nodesType_15_id = graphene.String()
    nodesType_15_name = graphene.String()
    nodesType_15_val = graphene.Int()
    nodesType_15_community = graphene.Int()
    nodesType_15_profile_url = graphene.String()

class nodesType_16(graphene.ObjectType):
    nodesType_16_id = graphene.String()
    nodesType_16_name = graphene.String()
    nodesType_16_val = graphene.Int()
    nodesType_16_community = graphene.Int()
    nodesType_16_profile_url = graphene.String()

class nodesType_17(graphene.ObjectType):
    nodesType_17_id = graphene.String()
    nodesType_17_name = graphene.String()
    nodesType_17_val = graphene.Int()
    nodesType_17_community = graphene.Int()
    nodesType_17_profile_url = graphene.String()

class nodesType_18(graphene.ObjectType):
    nodesType_18_id = graphene.String()
    nodesType_18_name = graphene.String()
    nodesType_18_val = graphene.Int()
    nodesType_18_community = graphene.Int()
    nodesType_18_profile_url = graphene.String()

class nodesType_19(graphene.ObjectType):
    nodesType_19_id = graphene.String()
    nodesType_19_name = graphene.String()
    nodesType_19_val = graphene.Int()
    nodesType_19_community = graphene.Int()
    nodesType_19_profile_url = graphene.String()

class nodesType_20(graphene.ObjectType):
    nodesType_20_id = graphene.String()
    nodesType_20_name = graphene.String()
    nodesType_20_val = graphene.Int()
    nodesType_20_community = graphene.Int()
    nodesType_20_profile_url = graphene.String()

class nodesType_21(graphene.ObjectType):
    nodesType_21_id = graphene.String()
    nodesType_21_name = graphene.String()
    nodesType_21_val = graphene.Int()
    nodesType_21_community = graphene.Int()
    nodesType_21_profile_url = graphene.String()

class nodesType_22(graphene.ObjectType):
    nodesType_22_id = graphene.String()
    nodesType_22_name = graphene.String()
    nodesType_22_val = graphene.Int()
    nodesType_22_community = graphene.Int()
    nodesType_22_profile_url = graphene.String()

class nodesType_23(graphene.ObjectType):
    nodesType_23_id = graphene.String()
    nodesType_23_name = graphene.String()
    nodesType_23_val = graphene.Int()
    nodesType_23_community = graphene.Int()
    nodesType_23_profile_url = graphene.String()

class nodesType_24(graphene.ObjectType):
    nodesType_24_id = graphene.String()
    nodesType_24_name = graphene.String()
    nodesType_24_val = graphene.Int()
    nodesType_24_community = graphene.Int()
    nodesType_24_profile_url = graphene.String()

class nodesType_25(graphene.ObjectType):
    nodesType_25_id = graphene.String()
    nodesType_25_name = graphene.String()
    nodesType_25_val = graphene.Int()
    nodesType_25_community = graphene.Int()
    nodesType_25_profile_url = graphene.String()

class nodesType_26(graphene.ObjectType):
    nodesType_26_id = graphene.String()
    nodesType_26_name = graphene.String()
    nodesType_26_val = graphene.Int()
    nodesType_26_community = graphene.Int()
    nodesType_26_profile_url = graphene.String()

class nodesType_27(graphene.ObjectType):
    nodesType_27_id = graphene.String()
    nodesType_27_name = graphene.String()
    nodesType_27_val = graphene.Int()
    nodesType_27_community = graphene.Int()
    nodesType_27_profile_url = graphene.String()

class nodesType_28(graphene.ObjectType):
    nodesType_28_id = graphene.String()
    nodesType_28_name = graphene.String()
    nodesType_28_val = graphene.Int()
    nodesType_28_community = graphene.Int()
    nodesType_28_profile_url = graphene.String()

class nodesType_29(graphene.ObjectType):
    nodesType_29_id = graphene.String()
    nodesType_29_name = graphene.String()
    nodesType_29_val = graphene.Int()
    nodesType_29_community = graphene.Int()
    nodesType_29_profile_url = graphene.String()

class nodesType_30(graphene.ObjectType):
    nodesType_30_id = graphene.String()
    nodesType_30_name = graphene.String()
    nodesType_30_val = graphene.Int()
    nodesType_30_community = graphene.Int()
    nodesType_30_profile_url = graphene.String()

class nodesType_31(graphene.ObjectType):
    nodesType_31_id = graphene.String()
    nodesType_31_name = graphene.String()
    nodesType_31_val = graphene.Int()
    nodesType_31_community = graphene.Int()
    nodesType_31_profile_url = graphene.String()

class nodesType_32(graphene.ObjectType):
    nodesType_32_id = graphene.String()
    nodesType_32_name = graphene.String()
    nodesType_32_val = graphene.Int()
    nodesType_32_community = graphene.Int()
    nodesType_32_profile_url = graphene.String()

class nodesType_33(graphene.ObjectType):
    nodesType_33_id = graphene.String()
    nodesType_33_name = graphene.String()
    nodesType_33_val = graphene.Int()
    nodesType_33_community = graphene.Int()
    nodesType_33_profile_url = graphene.String()

class nodesType_34(graphene.ObjectType):
    nodesType_34_id = graphene.String()
    nodesType_34_name = graphene.String()
    nodesType_34_val = graphene.Int()
    nodesType_34_community = graphene.Int()
    nodesType_34_profile_url = graphene.String()

class nodesType_35(graphene.ObjectType):
    nodesType_35_id = graphene.String()
    nodesType_35_name = graphene.String()
    nodesType_35_val = graphene.Int()
    nodesType_35_community = graphene.Int()
    nodesType_35_profile_url = graphene.String()

class nodesType_36(graphene.ObjectType):
    nodesType_36_id = graphene.String()
    nodesType_36_name = graphene.String()
    nodesType_36_val = graphene.Int()
    nodesType_36_community = graphene.Int()
    nodesType_36_profile_url = graphene.String()

class nodesType_37(graphene.ObjectType):
    nodesType_37_id = graphene.String()
    nodesType_37_name = graphene.String()
    nodesType_37_val = graphene.Int()
    nodesType_37_community = graphene.Int()
    nodesType_37_profile_url = graphene.String()

class nodesType_38(graphene.ObjectType):
    nodesType_38_id = graphene.String()
    nodesType_38_name = graphene.String()
    nodesType_38_val = graphene.Int()
    nodesType_38_community = graphene.Int()
    nodesType_38_profile_url = graphene.String()

class nodesType_39(graphene.ObjectType):
    nodesType_39_id = graphene.String()
    nodesType_39_name = graphene.String()
    nodesType_39_val = graphene.Int()
    nodesType_39_community = graphene.Int()
    nodesType_39_profile_url = graphene.String()

class nodesType_40(graphene.ObjectType):
    nodesType_40_id = graphene.String()
    nodesType_40_name = graphene.String()
    nodesType_40_val = graphene.Int()
    nodesType_40_community = graphene.Int()
    nodesType_40_profile_url = graphene.String()

class nodesType_41(graphene.ObjectType):
    nodesType_41_id = graphene.String()
    nodesType_41_name = graphene.String()
    nodesType_41_val = graphene.Int()
    nodesType_41_community = graphene.Int()
    nodesType_41_profile_url = graphene.String()

class nodesType_42(graphene.ObjectType):
    nodesType_42_id = graphene.String()
    nodesType_42_name = graphene.String()
    nodesType_42_val = graphene.Int()
    nodesType_42_community = graphene.Int()
    nodesType_42_profile_url = graphene.String()

class nodesType_43(graphene.ObjectType):
    nodesType_43_id = graphene.String()
    nodesType_43_name = graphene.String()
    nodesType_43_val = graphene.Int()
    nodesType_43_community = graphene.Int()
    nodesType_43_profile_url = graphene.String()

class nodesType_44(graphene.ObjectType):
    nodesType_44_id = graphene.String()
    nodesType_44_name = graphene.String()
    nodesType_44_val = graphene.Int()
    nodesType_44_community = graphene.Int()
    nodesType_44_profile_url = graphene.String()

class nodesType_45(graphene.ObjectType):
    nodesType_45_id = graphene.String()
    nodesType_45_name = graphene.String()
    nodesType_45_val = graphene.Int()
    nodesType_45_community = graphene.Int()
    nodesType_45_profile_url = graphene.String()

class nodesType_46(graphene.ObjectType):
    nodesType_46_id = graphene.String()
    nodesType_46_name = graphene.String()
    nodesType_46_val = graphene.Int()
    nodesType_46_community = graphene.Int()
    nodesType_46_profile_url = graphene.String()

class nodesType_47(graphene.ObjectType):
    nodesType_47_id = graphene.String()
    nodesType_47_name = graphene.String()
    nodesType_47_val = graphene.Int()
    nodesType_47_community = graphene.Int()
    nodesType_47_profile_url = graphene.String()

class nodesType_48(graphene.ObjectType):
    nodesType_48_id = graphene.String()
    nodesType_48_name = graphene.String()
    nodesType_48_val = graphene.Int()
    nodesType_48_community = graphene.Int()
    nodesType_48_profile_url = graphene.String()

class nodesType_49(graphene.ObjectType):
    nodesType_49_id = graphene.String()
    nodesType_49_name = graphene.String()
    nodesType_49_val = graphene.Int()
    nodesType_49_community = graphene.Int()
    nodesType_49_profile_url = graphene.String()

class nodesType_50(graphene.ObjectType):
    nodesType_50_id = graphene.String()
    nodesType_50_name = graphene.String()
    nodesType_50_val = graphene.Int()
    nodesType_50_community = graphene.Int()
    nodesType_50_profile_url = graphene.String()

class nodesType_51(graphene.ObjectType):
    nodesType_51_id = graphene.String()
    nodesType_51_name = graphene.String()
    nodesType_51_val = graphene.Int()
    nodesType_51_community = graphene.Int()
    nodesType_51_profile_url = graphene.String()

class nodesType_52(graphene.ObjectType):
    nodesType_52_id = graphene.String()
    nodesType_52_name = graphene.String()
    nodesType_52_val = graphene.Int()
    nodesType_52_community = graphene.Int()
    nodesType_52_profile_url = graphene.String()

class nodesType_53(graphene.ObjectType):
    nodesType_53_id = graphene.String()
    nodesType_53_name = graphene.String()
    nodesType_53_val = graphene.Int()
    nodesType_53_community = graphene.Int()
    nodesType_53_profile_url = graphene.String()

class linksType(graphene.ObjectType):
    linksType_0 = graphene.Field('linksType_0')
    linksType_1 = graphene.Field('linksType_1')
    linksType_2 = graphene.Field('linksType_2')
    linksType_3 = graphene.Field('linksType_3')
    linksType_4 = graphene.Field('linksType_4')
    linksType_5 = graphene.Field('linksType_5')
    linksType_6 = graphene.Field('linksType_6')
    linksType_7 = graphene.Field('linksType_7')
    linksType_8 = graphene.Field('linksType_8')
    linksType_9 = graphene.Field('linksType_9')
    linksType_10 = graphene.Field('linksType_10')
    linksType_11 = graphene.Field('linksType_11')
    linksType_12 = graphene.Field('linksType_12')
    linksType_13 = graphene.Field('linksType_13')
    linksType_14 = graphene.Field('linksType_14')
    linksType_15 = graphene.Field('linksType_15')
    linksType_16 = graphene.Field('linksType_16')
    linksType_17 = graphene.Field('linksType_17')
    linksType_18 = graphene.Field('linksType_18')
    linksType_19 = graphene.Field('linksType_19')
    linksType_20 = graphene.Field('linksType_20')
    linksType_21 = graphene.Field('linksType_21')
    linksType_22 = graphene.Field('linksType_22')
    linksType_23 = graphene.Field('linksType_23')
    linksType_24 = graphene.Field('linksType_24')
    linksType_25 = graphene.Field('linksType_25')
    linksType_26 = graphene.Field('linksType_26')
    linksType_27 = graphene.Field('linksType_27')
    linksType_28 = graphene.Field('linksType_28')
    linksType_29 = graphene.Field('linksType_29')
    linksType_30 = graphene.Field('linksType_30')
    linksType_31 = graphene.Field('linksType_31')
    linksType_32 = graphene.Field('linksType_32')
    linksType_33 = graphene.Field('linksType_33')
    linksType_34 = graphene.Field('linksType_34')
    linksType_35 = graphene.Field('linksType_35')
    linksType_36 = graphene.Field('linksType_36')
    linksType_37 = graphene.Field('linksType_37')
    linksType_38 = graphene.Field('linksType_38')
    linksType_39 = graphene.Field('linksType_39')
    linksType_40 = graphene.Field('linksType_40')
    linksType_41 = graphene.Field('linksType_41')
    linksType_42 = graphene.Field('linksType_42')
    linksType_43 = graphene.Field('linksType_43')
    linksType_44 = graphene.Field('linksType_44')
    linksType_45 = graphene.Field('linksType_45')
    linksType_46 = graphene.Field('linksType_46')
    linksType_47 = graphene.Field('linksType_47')
    linksType_48 = graphene.Field('linksType_48')
    linksType_49 = graphene.Field('linksType_49')
    linksType_50 = graphene.Field('linksType_50')
    linksType_51 = graphene.Field('linksType_51')
    linksType_52 = graphene.Field('linksType_52')

class linksType_0(graphene.ObjectType):
    linksType_0_source = graphene.String()
    linksType_0_target = graphene.String()
    linksType_0_full_text = graphene.String()
    linksType_0_topic = graphene.Field('DateTime')
    linksType_0_url_tweet = graphene.String()
    linksType_0_source_community = graphene.Int()
    linksType_0_target_community = graphene.Int()

class linksType_1(graphene.ObjectType):
    linksType_1_source = graphene.String()
    linksType_1_target = graphene.String()
    linksType_1_full_text = graphene.String()
    linksType_1_topic = graphene.Field('DateTime')
    linksType_1_url_tweet = graphene.String()
    linksType_1_source_community = graphene.Int()
    linksType_1_target_community = graphene.Int()

class linksType_2(graphene.ObjectType):
    linksType_2_source = graphene.String()
    linksType_2_target = graphene.String()
    linksType_2_full_text = graphene.String()
    linksType_2_topic = graphene.Field('DateTime')
    linksType_2_url_tweet = graphene.String()
    linksType_2_source_community = graphene.Int()
    linksType_2_target_community = graphene.Int()

class linksType_3(graphene.ObjectType):
    linksType_3_source = graphene.String()
    linksType_3_target = graphene.String()
    linksType_3_full_text = graphene.String()
    linksType_3_topic = graphene.Field('DateTime')
    linksType_3_url_tweet = graphene.String()
    linksType_3_source_community = graphene.Int()
    linksType_3_target_community = graphene.Int()

class linksType_4(graphene.ObjectType):
    linksType_4_source = graphene.String()
    linksType_4_target = graphene.String()
    linksType_4_full_text = graphene.String()
    linksType_4_topic = graphene.Field('DateTime')
    linksType_4_url_tweet = graphene.String()
    linksType_4_source_community = graphene.Int()
    linksType_4_target_community = graphene.Int()

class linksType_5(graphene.ObjectType):
    linksType_5_source = graphene.String()
    linksType_5_target = graphene.String()
    linksType_5_full_text = graphene.String()
    linksType_5_topic = graphene.Field('DateTime')
    linksType_5_url_tweet = graphene.String()
    linksType_5_source_community = graphene.Int()
    linksType_5_target_community = graphene.Int()

class linksType_6(graphene.ObjectType):
    linksType_6_source = graphene.String()
    linksType_6_target = graphene.String()
    linksType_6_full_text = graphene.String()
    linksType_6_topic = graphene.Field('DateTime')
    linksType_6_url_tweet = graphene.String()
    linksType_6_source_community = graphene.Int()
    linksType_6_target_community = graphene.Int()

class linksType_7(graphene.ObjectType):
    linksType_7_source = graphene.String()
    linksType_7_target = graphene.String()
    linksType_7_full_text = graphene.String()
    linksType_7_topic = graphene.Field('DateTime')
    linksType_7_url_tweet = graphene.String()
    linksType_7_source_community = graphene.Int()
    linksType_7_target_community = graphene.Int()

class linksType_8(graphene.ObjectType):
    linksType_8_source = graphene.String()
    linksType_8_target = graphene.String()
    linksType_8_full_text = graphene.String()
    linksType_8_topic = graphene.Field('DateTime')
    linksType_8_url_tweet = graphene.String()
    linksType_8_source_community = graphene.Int()
    linksType_8_target_community = graphene.Int()

class linksType_9(graphene.ObjectType):
    linksType_9_source = graphene.String()
    linksType_9_target = graphene.String()
    linksType_9_full_text = graphene.String()
    linksType_9_topic = graphene.Field('DateTime')
    linksType_9_url_tweet = graphene.String()
    linksType_9_source_community = graphene.Int()
    linksType_9_target_community = graphene.Int()

class linksType_10(graphene.ObjectType):
    linksType_10_source = graphene.String()
    linksType_10_target = graphene.String()
    linksType_10_full_text = graphene.String()
    linksType_10_topic = graphene.Field('DateTime')
    linksType_10_url_tweet = graphene.String()
    linksType_10_source_community = graphene.Int()
    linksType_10_target_community = graphene.Int()

class linksType_11(graphene.ObjectType):
    linksType_11_source = graphene.String()
    linksType_11_target = graphene.String()
    linksType_11_full_text = graphene.String()
    linksType_11_topic = graphene.Field('DateTime')
    linksType_11_url_tweet = graphene.String()
    linksType_11_source_community = graphene.Int()
    linksType_11_target_community = graphene.Int()

class linksType_12(graphene.ObjectType):
    linksType_12_source = graphene.String()
    linksType_12_target = graphene.String()
    linksType_12_full_text = graphene.String()
    linksType_12_topic = graphene.Field('DateTime')
    linksType_12_url_tweet = graphene.String()
    linksType_12_source_community = graphene.Int()
    linksType_12_target_community = graphene.Int()

class linksType_13(graphene.ObjectType):
    linksType_13_source = graphene.String()
    linksType_13_target = graphene.String()
    linksType_13_full_text = graphene.String()
    linksType_13_topic = graphene.Field('DateTime')
    linksType_13_url_tweet = graphene.String()
    linksType_13_source_community = graphene.Int()
    linksType_13_target_community = graphene.Int()

class linksType_14(graphene.ObjectType):
    linksType_14_source = graphene.String()
    linksType_14_target = graphene.String()
    linksType_14_full_text = graphene.String()
    linksType_14_topic = graphene.Field('DateTime')
    linksType_14_url_tweet = graphene.String()
    linksType_14_source_community = graphene.Int()
    linksType_14_target_community = graphene.Int()

class linksType_15(graphene.ObjectType):
    linksType_15_source = graphene.String()
    linksType_15_target = graphene.String()
    linksType_15_full_text = graphene.String()
    linksType_15_topic = graphene.Field('DateTime')
    linksType_15_url_tweet = graphene.String()
    linksType_15_source_community = graphene.Int()
    linksType_15_target_community = graphene.Int()

class linksType_16(graphene.ObjectType):
    linksType_16_source = graphene.String()
    linksType_16_target = graphene.String()
    linksType_16_full_text = graphene.String()
    linksType_16_topic = graphene.Field('DateTime')
    linksType_16_url_tweet = graphene.String()
    linksType_16_source_community = graphene.Int()
    linksType_16_target_community = graphene.Int()

class linksType_17(graphene.ObjectType):
    linksType_17_source = graphene.String()
    linksType_17_target = graphene.String()
    linksType_17_full_text = graphene.String()
    linksType_17_topic = graphene.Field('DateTime')
    linksType_17_url_tweet = graphene.String()
    linksType_17_source_community = graphene.Int()
    linksType_17_target_community = graphene.Int()

class linksType_18(graphene.ObjectType):
    linksType_18_source = graphene.String()
    linksType_18_target = graphene.String()
    linksType_18_full_text = graphene.String()
    linksType_18_topic = graphene.Field('DateTime')
    linksType_18_url_tweet = graphene.String()
    linksType_18_source_community = graphene.Int()
    linksType_18_target_community = graphene.Int()

class linksType_19(graphene.ObjectType):
    linksType_19_source = graphene.String()
    linksType_19_target = graphene.String()
    linksType_19_full_text = graphene.String()
    linksType_19_topic = graphene.Field('DateTime')
    linksType_19_url_tweet = graphene.String()
    linksType_19_source_community = graphene.Int()
    linksType_19_target_community = graphene.Int()

class linksType_20(graphene.ObjectType):
    linksType_20_source = graphene.String()
    linksType_20_target = graphene.String()
    linksType_20_full_text = graphene.String()
    linksType_20_topic = graphene.Field('DateTime')
    linksType_20_url_tweet = graphene.String()
    linksType_20_source_community = graphene.Int()
    linksType_20_target_community = graphene.Int()

class linksType_21(graphene.ObjectType):
    linksType_21_source = graphene.String()
    linksType_21_target = graphene.String()
    linksType_21_full_text = graphene.String()
    linksType_21_topic = graphene.Field('DateTime')
    linksType_21_url_tweet = graphene.String()
    linksType_21_source_community = graphene.Int()
    linksType_21_target_community = graphene.Int()

class linksType_22(graphene.ObjectType):
    linksType_22_source = graphene.String()
    linksType_22_target = graphene.String()
    linksType_22_full_text = graphene.String()
    linksType_22_topic = graphene.Field('DateTime')
    linksType_22_url_tweet = graphene.String()
    linksType_22_source_community = graphene.Int()
    linksType_22_target_community = graphene.Int()

class linksType_23(graphene.ObjectType):
    linksType_23_source = graphene.String()
    linksType_23_target = graphene.String()
    linksType_23_full_text = graphene.String()
    linksType_23_topic = graphene.Field('DateTime')
    linksType_23_url_tweet = graphene.String()
    linksType_23_source_community = graphene.Int()
    linksType_23_target_community = graphene.Int()

class linksType_24(graphene.ObjectType):
    linksType_24_source = graphene.String()
    linksType_24_target = graphene.String()
    linksType_24_full_text = graphene.String()
    linksType_24_topic = graphene.Field('DateTime')
    linksType_24_url_tweet = graphene.String()
    linksType_24_source_community = graphene.Int()
    linksType_24_target_community = graphene.Int()

class linksType_25(graphene.ObjectType):
    linksType_25_source = graphene.String()
    linksType_25_target = graphene.String()
    linksType_25_full_text = graphene.String()
    linksType_25_topic = graphene.Field('DateTime')
    linksType_25_url_tweet = graphene.String()
    linksType_25_source_community = graphene.Int()
    linksType_25_target_community = graphene.Int()

class linksType_26(graphene.ObjectType):
    linksType_26_source = graphene.String()
    linksType_26_target = graphene.String()
    linksType_26_full_text = graphene.String()
    linksType_26_topic = graphene.Field('DateTime')
    linksType_26_url_tweet = graphene.String()
    linksType_26_source_community = graphene.Int()
    linksType_26_target_community = graphene.Int()

class linksType_27(graphene.ObjectType):
    linksType_27_source = graphene.String()
    linksType_27_target = graphene.String()
    linksType_27_full_text = graphene.String()
    linksType_27_topic = graphene.Field('DateTime')
    linksType_27_url_tweet = graphene.String()
    linksType_27_source_community = graphene.Int()
    linksType_27_target_community = graphene.Int()

class linksType_28(graphene.ObjectType):
    linksType_28_source = graphene.String()
    linksType_28_target = graphene.String()
    linksType_28_full_text = graphene.String()
    linksType_28_topic = graphene.Field('DateTime')
    linksType_28_url_tweet = graphene.String()
    linksType_28_source_community = graphene.Int()
    linksType_28_target_community = graphene.Int()

class linksType_29(graphene.ObjectType):
    linksType_29_source = graphene.String()
    linksType_29_target = graphene.String()
    linksType_29_full_text = graphene.String()
    linksType_29_topic = graphene.Field('DateTime')
    linksType_29_url_tweet = graphene.String()
    linksType_29_source_community = graphene.Int()
    linksType_29_target_community = graphene.Int()

class linksType_30(graphene.ObjectType):
    linksType_30_source = graphene.String()
    linksType_30_target = graphene.String()
    linksType_30_full_text = graphene.String()
    linksType_30_topic = graphene.Field('DateTime')
    linksType_30_url_tweet = graphene.String()
    linksType_30_source_community = graphene.Int()
    linksType_30_target_community = graphene.Int()

class linksType_31(graphene.ObjectType):
    linksType_31_source = graphene.String()
    linksType_31_target = graphene.String()
    linksType_31_full_text = graphene.String()
    linksType_31_topic = graphene.Field('DateTime')
    linksType_31_url_tweet = graphene.String()
    linksType_31_source_community = graphene.Int()
    linksType_31_target_community = graphene.Int()

class linksType_32(graphene.ObjectType):
    linksType_32_source = graphene.String()
    linksType_32_target = graphene.String()
    linksType_32_full_text = graphene.String()
    linksType_32_topic = graphene.Field('DateTime')
    linksType_32_url_tweet = graphene.String()
    linksType_32_source_community = graphene.Int()
    linksType_32_target_community = graphene.Int()

class linksType_33(graphene.ObjectType):
    linksType_33_source = graphene.String()
    linksType_33_target = graphene.String()
    linksType_33_full_text = graphene.String()
    linksType_33_topic = graphene.Field('DateTime')
    linksType_33_url_tweet = graphene.String()
    linksType_33_source_community = graphene.Int()
    linksType_33_target_community = graphene.Int()

class linksType_34(graphene.ObjectType):
    linksType_34_source = graphene.String()
    linksType_34_target = graphene.String()
    linksType_34_full_text = graphene.String()
    linksType_34_topic = graphene.Field('DateTime')
    linksType_34_url_tweet = graphene.String()
    linksType_34_source_community = graphene.Int()
    linksType_34_target_community = graphene.Int()

class linksType_35(graphene.ObjectType):
    linksType_35_source = graphene.String()
    linksType_35_target = graphene.String()
    linksType_35_full_text = graphene.String()
    linksType_35_topic = graphene.Field('DateTime')
    linksType_35_url_tweet = graphene.String()
    linksType_35_source_community = graphene.Int()
    linksType_35_target_community = graphene.Int()

class linksType_36(graphene.ObjectType):
    linksType_36_source = graphene.String()
    linksType_36_target = graphene.String()
    linksType_36_full_text = graphene.String()
    linksType_36_topic = graphene.Field('DateTime')
    linksType_36_url_tweet = graphene.String()
    linksType_36_source_community = graphene.Int()
    linksType_36_target_community = graphene.Int()

class linksType_37(graphene.ObjectType):
    linksType_37_source = graphene.String()
    linksType_37_target = graphene.String()
    linksType_37_full_text = graphene.String()
    linksType_37_topic = graphene.Field('DateTime')
    linksType_37_url_tweet = graphene.String()
    linksType_37_source_community = graphene.Int()
    linksType_37_target_community = graphene.Int()

class linksType_38(graphene.ObjectType):
    linksType_38_source = graphene.String()
    linksType_38_target = graphene.String()
    linksType_38_full_text = graphene.String()
    linksType_38_topic = graphene.Field('DateTime')
    linksType_38_url_tweet = graphene.String()
    linksType_38_source_community = graphene.Int()
    linksType_38_target_community = graphene.Int()

class linksType_39(graphene.ObjectType):
    linksType_39_source = graphene.String()
    linksType_39_target = graphene.String()
    linksType_39_full_text = graphene.String()
    linksType_39_topic = graphene.Field('DateTime')
    linksType_39_url_tweet = graphene.String()
    linksType_39_source_community = graphene.Int()
    linksType_39_target_community = graphene.Int()

class linksType_40(graphene.ObjectType):
    linksType_40_source = graphene.String()
    linksType_40_target = graphene.String()
    linksType_40_full_text = graphene.String()
    linksType_40_topic = graphene.Field('DateTime')
    linksType_40_url_tweet = graphene.String()
    linksType_40_source_community = graphene.Int()
    linksType_40_target_community = graphene.Int()

class linksType_41(graphene.ObjectType):
    linksType_41_source = graphene.String()
    linksType_41_target = graphene.String()
    linksType_41_full_text = graphene.String()
    linksType_41_topic = graphene.Field('DateTime')
    linksType_41_url_tweet = graphene.String()
    linksType_41_source_community = graphene.Int()
    linksType_41_target_community = graphene.Int()

class linksType_42(graphene.ObjectType):
    linksType_42_source = graphene.String()
    linksType_42_target = graphene.String()
    linksType_42_full_text = graphene.String()
    linksType_42_topic = graphene.Field('DateTime')
    linksType_42_url_tweet = graphene.String()
    linksType_42_source_community = graphene.Int()
    linksType_42_target_community = graphene.Int()

class linksType_43(graphene.ObjectType):
    linksType_43_source = graphene.String()
    linksType_43_target = graphene.String()
    linksType_43_full_text = graphene.String()
    linksType_43_topic = graphene.Field('DateTime')
    linksType_43_url_tweet = graphene.String()
    linksType_43_source_community = graphene.Int()
    linksType_43_target_community = graphene.Int()

class linksType_44(graphene.ObjectType):
    linksType_44_source = graphene.String()
    linksType_44_target = graphene.String()
    linksType_44_full_text = graphene.String()
    linksType_44_topic = graphene.Field('DateTime')
    linksType_44_url_tweet = graphene.String()
    linksType_44_source_community = graphene.Int()
    linksType_44_target_community = graphene.Int()

class linksType_45(graphene.ObjectType):
    linksType_45_source = graphene.String()
    linksType_45_target = graphene.String()
    linksType_45_full_text = graphene.String()
    linksType_45_topic = graphene.Field('DateTime')
    linksType_45_url_tweet = graphene.String()
    linksType_45_source_community = graphene.Int()
    linksType_45_target_community = graphene.Int()

class linksType_46(graphene.ObjectType):
    linksType_46_source = graphene.String()
    linksType_46_target = graphene.String()
    linksType_46_full_text = graphene.String()
    linksType_46_topic = graphene.Field('DateTime')
    linksType_46_url_tweet = graphene.String()
    linksType_46_source_community = graphene.Int()
    linksType_46_target_community = graphene.Int()

class linksType_47(graphene.ObjectType):
    linksType_47_source = graphene.String()
    linksType_47_target = graphene.String()
    linksType_47_full_text = graphene.String()
    linksType_47_topic = graphene.Field('DateTime')
    linksType_47_url_tweet = graphene.String()
    linksType_47_source_community = graphene.Int()
    linksType_47_target_community = graphene.Int()

class linksType_48(graphene.ObjectType):
    linksType_48_source = graphene.String()
    linksType_48_target = graphene.String()
    linksType_48_full_text = graphene.String()
    linksType_48_topic = graphene.Field('DateTime')
    linksType_48_url_tweet = graphene.String()
    linksType_48_source_community = graphene.Int()
    linksType_48_target_community = graphene.Int()

class linksType_49(graphene.ObjectType):
    linksType_49_source = graphene.String()
    linksType_49_target = graphene.String()
    linksType_49_full_text = graphene.String()
    linksType_49_topic = graphene.Field('DateTime')
    linksType_49_url_tweet = graphene.String()
    linksType_49_source_community = graphene.Int()
    linksType_49_target_community = graphene.Int()

class linksType_50(graphene.ObjectType):
    linksType_50_source = graphene.String()
    linksType_50_target = graphene.String()
    linksType_50_full_text = graphene.String()
    linksType_50_topic = graphene.Field('DateTime')
    linksType_50_url_tweet = graphene.String()
    linksType_50_source_community = graphene.Int()
    linksType_50_target_community = graphene.Int()

class linksType_51(graphene.ObjectType):
    linksType_51_source = graphene.String()
    linksType_51_target = graphene.String()
    linksType_51_full_text = graphene.String()
    linksType_51_topic = graphene.Field('DateTime')
    linksType_51_url_tweet = graphene.String()
    linksType_51_source_community = graphene.Int()
    linksType_51_target_community = graphene.Int()

class linksType_52(graphene.ObjectType):
    linksType_52_source = graphene.String()
    linksType_52_target = graphene.String()
    linksType_52_full_text = graphene.String()
    linksType_52_topic = graphene.Field('DateTime')
    linksType_52_url_tweet = graphene.String()
    linksType_52_source_community = graphene.Int()
    linksType_52_target_community = graphene.Int()

class community(graphene.ObjectType):
    id = graphene.ID()
    projectId = graphene.String()
    nodes = graphene.Field('nodesType')
    links = graphene.Field('linksType')

