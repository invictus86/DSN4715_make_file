import os


def modify_file(old_file_path, new_file_path, dict_old_new_str):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            for old_str, new_str in dict_old_new_str.items():
                line = line.replace(old_str, new_str)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


# def modify_file_version10(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
#                           old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7, new_str7,
#                           old_str8, new_str8, old_str9, new_str9, old_str10, new_str10):
#     with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
#         for line in f1:
#             if old_str1 in line:
#                 line = line.replace(old_str1, new_str1)
#             if old_str2 in line:
#                 print old_str2, new_str2
#                 line = line.replace(old_str2, new_str2)
#             if old_str3 in line:
#                 line = line.replace(old_str3, new_str3)
#             if old_str4 in line:
#                 line = line.replace(old_str4, new_str4)
#             if old_str5 in line:
#                 line = line.replace(old_str5, new_str5)
#             if old_str6 in line:
#                 line = line.replace(old_str6, new_str6)
#             if old_str7 in line:
#                 line = line.replace(old_str7, new_str7)
#             if old_str8 in line:
#                 line = line.replace(old_str8, new_str8)
#             if old_str9 in line:
#                 line = line.replace(old_str9, new_str9)
#             if old_str10 in line:
#                 line = line.replace(old_str10, new_str10)
#             f2.write(line)
#     print "generate new file {} success".format(new_file_path)
#
#
# def modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
#                           old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7, new_str7,
#                           old_str8, new_str8, old_str9, new_str9, old_str10, new_str10, old_str11, new_str11):
#     with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
#         for line in f1:
#             if old_str1 in line:
#                 line = line.replace(old_str1, new_str1)
#             if old_str2 in line:
#                 print old_str2, new_str2
#                 line = line.replace(old_str2, new_str2)
#             if old_str3 in line:
#                 line = line.replace(old_str3, new_str3)
#             if old_str4 in line:
#                 line = line.replace(old_str4, new_str4)
#             if old_str5 in line:
#                 line = line.replace(old_str5, new_str5)
#             if old_str6 in line:
#                 line = line.replace(old_str6, new_str6)
#             if old_str7 in line:
#                 line = line.replace(old_str7, new_str7)
#             if old_str8 in line:
#                 line = line.replace(old_str8, new_str8)
#             if old_str9 in line:
#                 line = line.replace(old_str9, new_str9)
#             if old_str10 in line:
#                 line = line.replace(old_str10, new_str10)
#             if old_str11 in line:
#                 line = line.replace(old_str11, new_str11)
#             f2.write(line)
#     print "generate new file {} success".format(new_file_path)
#
#
# def modify_file_version12(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
#                           old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7, new_str7,
#                           old_str8, new_str8, old_str9, new_str9, old_str10, new_str10, old_str11, new_str11, old_str12,
#                           new_str12):
#     with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
#         for line in f1:
#             if old_str1 in line:
#                 line = line.replace(old_str1, new_str1)
#             if old_str2 in line:
#                 print old_str2, new_str2
#                 line = line.replace(old_str2, new_str2)
#             if old_str3 in line:
#                 line = line.replace(old_str3, new_str3)
#             if old_str4 in line:
#                 line = line.replace(old_str4, new_str4)
#             if old_str5 in line:
#                 line = line.replace(old_str5, new_str5)
#             if old_str6 in line:
#                 line = line.replace(old_str6, new_str6)
#             if old_str7 in line:
#                 line = line.replace(old_str7, new_str7)
#             if old_str8 in line:
#                 line = line.replace(old_str8, new_str8)
#             if old_str9 in line:
#                 line = line.replace(old_str9, new_str9)
#             if old_str10 in line:
#                 line = line.replace(old_str10, new_str10)
#             if old_str11 in line:
#                 line = line.replace(old_str11, new_str11)
#             if old_str12 in line:
#                 line = line.replace(old_str12, new_str12)
#             f2.write(line)
#     print "generate new file {} success".format(new_file_path)


def make_special_bootlogo_file():
    new_str_dict = {1200: 1200, 1201: 1201, 1202: 1202, 1203: 1203, 1204: 1204, 1205: 1205, 1100: 1100, 1101: 1101,
                    1102: 1102, 1103: 1103, 1104: 1104}
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-specil-{}.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        if dsn_ver == 1200:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 final_white_bootlogo.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1201:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 final_black_bootlogo.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1202:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loaderres_white.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1203:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loaderres_black.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1204:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 white_bootlogo_changestring_nocircle.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1205:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loaderres_changeerrocode.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1100:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'.format(dsn_ver)
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'.format(dsn_ver)

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1101:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "5 fsi.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'.format(dsn_ver)
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'.format(dsn_ver)

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1102:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'.format(dsn_ver)
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'.format(dsn_ver)

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1103:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "23 tee.aes 1 {}""'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'.format(dsn_ver)
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'.format(dsn_ver)

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

        elif dsn_ver == 1104:
            new_file_path = new_file_path.format(dsn_ver)
            new_str1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loader_resource.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ""
            new_str5 = ""
            new_str6 = ""
            new_str7 = ""
            new_str8 = ""

            new_str9 = 'USBOutputFile "UpgradeFile.bin"'.format(dsn_ver)
            new_str10 = 'OTAOutputFile "UpgradeFile.ts"'.format(dsn_ver)

            dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                                old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                                old_str9: new_str9, old_str10: new_str10}
            modify_file(old_file_path, new_file_path, dict_old_new_str)
            new_file_path = "./GenerateUpgImage-specil-{}.cfg"

            print "streantool file Generate complete"


def make_app_bootlogo_file():
    list_version = [[999, 999, 999, 999, 999, 999], [999, 1000, 1000, 1000, 1000, 1000],
                    [999, 1001, 1001, 1001, 1001, 1001], [1000, 999, 999, 999, 999, 999],
                    [1000, 1000, 1000, 1000, 1000, 1000], [1000, 1001, 1001, 1001, 1001, 1001],
                    [1001, 999, 999, 999, 999, 999], [1001, 1000, 1000, 1000, 1000, 1000],
                    [1001, 1001, 1001, 1001, 1001, 1001], [65535, 65535, 65535, 65535, 65535, 65535]]

    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-{}-{}.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'

    for [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] in list_version:
        new_file_path = new_file_path.format(dsn_ver, vmlinux_ver)
        new_str1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 6'

        new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
        new_str6 = 'InputFile4 "23 tee.aes 1 {}"'.format(see_ver)
        new_str7 = 'InputFile5 "7 loader_resource.bin 1 {}"'.format(cfg_ver)
        new_str8 = 'InputFile6 "24 bl31.aes 1 {}"'.format(cfg_ver)

        new_str9 = 'USBOutputFile "UpgradeFile.bin"'.format(dsn_ver, vmlinux_ver)
        new_str10 = 'OTAOutputFile "UpgradeFile.ts"'.format(dsn_ver, vmlinux_ver)

        dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                            old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                            old_str9: new_str9, old_str10: new_str10}
        modify_file(old_file_path, new_file_path, dict_old_new_str)
        new_file_path = "./GenerateUpgImage-{}-{}.cfg"


def make_incorrect_hardversion():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-incorrect-hardver.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'HardWareNo 29'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version

    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'HardWareNo 99'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)

    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


def make_incorrect_oui():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-incorrect-oui.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'ManuCode 13416689'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version
    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'ManuCode 99999999'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


# def make_unsigend_app():
#     old_file_path = "./streamtool.cfg"
#     new_file_path = "./streamtool-unsigned-app.cfg"
#
#     old_str1 = "SoftWareNo 1016"
#     old_str5 = 'USBOutputFile "UpgradeFile.bin"'
#     old_str6 = 'OTAOutputFile "UpgradeFile.ts"'
#
#     new_str1 = "SoftWareNo 15000"
#     new_str5 = 'USBOutputFile "./7414-v2/unsigned_application/UpgradeFile.bin"'
#     new_str6 = 'OTAOutputFile "./7414-v2/unsigned_application/UpgradeFile.ts"'
#
#     modify_file_version1(old_file_path, new_file_path, old_str1, new_str1, old_str5, new_str5, old_str6,
#                          new_str6)


def make_wrong_sigend():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-wrong-signed.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'AppRSAPrivateKey "app_privatekey.bin"'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version

    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'AppRSAPrivateKey "privatekey.bin"'
    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


def make_incorrect_manufacturedes():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-incorrect-manufacturedes.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'ManufactureDes "EKT"'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version
    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'ManufactureDes "KKK111"'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


def make_incorrect_machinedes():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-incorrect-machinedes.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'ModelNo "DSN4715"'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version
    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'ModelNo "DSN4715111"'
    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


def make_downloadpid_1030_tableid_0():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-downloadpid-1030-tableid-1.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'DownLoadPID 1026'
    old_str12 = 'TableID 1'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version

    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'DownLoadPID 1030'
    new_str12 = 'TableID 0'
    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11, old_str12: new_str12}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version12(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11, old_str90, new_str90)

    print "streantool file Generate complete"


def make_dsi_crc():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-dsi-crc.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'DSI_CRC_Error_Test_Flag 0'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version
    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'DSI_CRC_Error_Test_Flag 1'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


def make_dii_crc():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-dii-crc.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'DII_CRC_Error_Test_Flag 0'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version
    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'DII_CRC_Error_Test_Flag 1'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


def make_ddb_crc():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-ddb-crc.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'DDB_CRC_Error_Test_Flag 0'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version
    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'DDB_CRC_Error_Test_Flag 1'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


def make_downloadheader_crc():
    list_version = [15000, 15000, 15000, 15000, 15000, 15000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-downloadheader-crc.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str11 = 'DownloadHeader_CRC_Error_Test_Flag 0'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version
    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 fsi.uImage 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'
    new_str11 = 'DownloadHeader_CRC_Error_Test_Flag 1'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10, old_str11: new_str11}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    # modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3,
    #                       new_str3, old_str4, new_str4, old_str5, new_str5, old_str6, new_str6, old_str7,
    #                       new_str7, old_str9, new_str9, old_str10, new_str10, old_str8, new_str8, old_str11,
    #                       new_str11)

    print "streantool file Generate complete"


def make_big_file():
    list_version = [10000, 10000, 10000, 10000, 10000, 10000]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-big.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version
    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 3'

    new_str3 = 'InputFile1 "4 big_vmlinux_size.bin 1 {}"'.format(vmlinux_ver)
    new_str4 = 'InputFile2 "5 big_fsi_size.bin 2 {}"'.format(fsi_ver)
    new_str5 = 'InputFile3 "6 big_bootlogo_size.bin 1 {}"'.format(bootlogo_ver)
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    print "streantool file Generate complete"


def make_excessive_big_file():
    list_version = [10003, 10003, 10003, 10003, 10003, 10003]
    old_file_path = "./GenerateUpgImage.cfg"
    new_file_path = "./GenerateUpgImage-excessive-big.cfg"
    old_str1 = "DSN 7"
    old_str2 = 'InputFileNumber 6'

    old_str3 = 'InputFile1 "4 fsi.uImage 1 7"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 7"'
    old_str5 = 'InputFile3 "6 bootlogo.bin 1 7"'
    old_str6 = 'InputFile4 "23 tee.aes 1 7"'
    old_str7 = 'InputFile5 "7 loader_resource.bin 1 7"'
    old_str8 = 'InputFile6 "24 bl31.aes 1 7"'

    old_str9 = 'USBOutputFile "UpgradeFile.bin"'
    old_str10 = 'OTAOutputFile "UpgradeFile.ts"'

    [dsn_ver, vmlinux_ver, fsi_ver, bootlogo_ver, see_ver, cfg_ver] = list_version

    new_str1 = "DSN {}".format(dsn_ver)
    new_str2 = 'InputFileNumber 1'

    new_str3 = 'InputFile1 "4 excessive_big_vmlinux_size.bin 1 {}"'.format(vmlinux_ver)
    # new_str4 = 'InputFile2 "5 excessive_big_fsi_size.bin 1 {}"'.format(fsi_ver)
    new_str4 = ""
    # new_str5 = 'InputFile3 "6 excessive_big_bootlogo_size.bin 1 {}"'.format(bootlogo_ver)
    new_str5 = ""
    new_str6 = ""
    new_str7 = ""
    new_str8 = ""

    new_str9 = 'USBOutputFile "UpgradeFile.bin"'
    new_str10 = 'OTAOutputFile "UpgradeFile.ts"'

    dict_old_new_str = {old_str1: new_str1, old_str2: new_str2, old_str3: new_str3, old_str4: new_str4,
                        old_str5: new_str5, old_str6: new_str6, old_str7: new_str7, old_str8: new_str8,
                        old_str9: new_str9, old_str10: new_str10}
    modify_file(old_file_path, new_file_path, dict_old_new_str)
    print "streantool file Generate complete"


def create_folder(folder_name):
    """
    base current floder, creat folder
    :param folder_name: folder name (str)
    :return: None
    """
    curPath = os.getcwd()
    tempPath = folder_name
    targetPath = curPath + os.path.sep + tempPath
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    else:
        print "file already exists!"


if __name__ == '__main__':
    create_folder("./DSN4715")
    create_folder("./DSN4715/999")
    create_folder("./DSN4715/999/999")
    create_folder("./DSN4715/999/1000")
    create_folder("./DSN4715/999/1001")
    create_folder("./DSN4715/1000")
    create_folder("./DSN4715/1000/999")
    create_folder("./DSN4715/1000/1000")
    create_folder("./DSN4715/1000/1001")
    create_folder("./DSN4715/1001")
    create_folder("./DSN4715/1001/999")
    create_folder("./DSN4715/1001/1000")
    create_folder("./DSN4715/1001/1001")
    create_folder("./DSN4715/65535")
    create_folder("./DSN4715/65535/65535")

    create_folder("./DSN4715/incorrect_hardware")
    create_folder("./DSN4715/incorrect_oui")
    create_folder("./DSN4715/wrong_signed")
    create_folder("./DSN4715/incorrect_manuf")
    create_folder("./DSN4715/incorrect_machinedes")
    create_folder("./DSN4715/downloadpid_1030_tableid_0")
    create_folder("./DSN4715/dsi_crc")
    create_folder("./DSN4715/dii_crc")
    create_folder("./DSN4715/ddb_crc")
    create_folder("./DSN4715/downloadheader_crc")
    create_folder("./DSN4715/big_size")
    create_folder("./DSN4715/excessive_big_size")

    create_folder("./DSN4715/unisgned_file")

    create_folder("./DSN4715/loader_resource_black")
    create_folder("./DSN4715/loader_resource_white")
    create_folder("./DSN4715/bootlogo_black_no_progress")
    create_folder("./DSN4715/bootlogo_white")
    create_folder("./DSN4715/boot_err_code")
    create_folder("./DSN4715/portion")
    create_folder("./DSN4715/portion/1100")
    create_folder("./DSN4715/portion/1101")
    create_folder("./DSN4715/portion/1102")
    create_folder("./DSN4715/portion/1103")
    create_folder("./DSN4715/portion/1104")
    create_folder("./DSN4715/sys_info_module_update")
    create_folder("./DSN4715/loader_err_code")

    make_app_bootlogo_file()
    make_incorrect_hardversion()
    make_incorrect_oui()
    make_wrong_sigend()
    make_incorrect_manufacturedes()
    make_incorrect_machinedes()
    make_downloadpid_1030_tableid_0()
    make_dsi_crc()
    make_dii_crc()
    make_ddb_crc()
    make_downloadheader_crc()
    make_big_file()
    make_excessive_big_file()
    make_special_bootlogo_file()
