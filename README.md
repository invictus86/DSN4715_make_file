auto make file
=========

DSN4715 make file

generic loader做文件时使用，对应模块文件如下
=========
InputFile1 "4 fsi.uImage 1 7"
InputFile2 "5 fsi.bin 1 7"
InputFile3 "6 bootlogo.bin 1 7"
InputFile4 "23 tee.aes 1 7"
InputFile5 "7 loader_resource.bin 1 7"
InputFile6 "24 bl31.aes 1 7"

注意输入文件名如果与GenerateUpgImage.cfg中输入文件名称不一致，需修改输入文件名称，并要确保文件完整性

针对其他型号的loader在使用此脚本时需进行修改，主要适配如下设置项：
1、模块文件数及Module_Index，此模板为6个模块
2、ModelNo
3、HardWareNo
建议先使用beyond compare工具对比，按照模板格式进行修改