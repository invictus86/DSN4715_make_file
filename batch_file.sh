#!/usr/bin/env bash
cd make_big_file
./batch_big_file.sh
cd ../
python generate_file_streamtool.py
./GenerateUSBUpgImage GenerateUpgImage-999-999.cfg
./GenerateOTAUpgImage GenerateUpgImage-999-999.cfg
mv ./UpgradeFile.bin ./DSN4715/999/999/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/999/999/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-999-1000.cfg
./GenerateOTAUpgImage GenerateUpgImage-999-1000.cfg
mv ./UpgradeFile.bin ./DSN4715/999/1000/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/999/1000/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-999-1001.cfg
./GenerateOTAUpgImage GenerateUpgImage-999-1001.cfg
mv ./UpgradeFile.bin ./DSN4715/999/1001/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/999/1001/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-1000-999.cfg
./GenerateOTAUpgImage GenerateUpgImage-1000-999.cfg
mv ./UpgradeFile.bin ./DSN4715/1000/999/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/1000/999/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-1000-1000.cfg
./GenerateOTAUpgImage GenerateUpgImage-1000-1000.cfg
mv ./UpgradeFile.bin ./DSN4715/1000/1000/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/1000/1000/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-1000-1001.cfg
./GenerateOTAUpgImage GenerateUpgImage-1000-1001.cfg
mv ./UpgradeFile.bin ./DSN4715/1000/1001/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/1000/1001/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-1001-999.cfg
./GenerateOTAUpgImage GenerateUpgImage-1001-999.cfg
mv ./UpgradeFile.bin ./DSN4715/1001/999/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/1001/999/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-1001-1000.cfg
./GenerateOTAUpgImage GenerateUpgImage-1001-1000.cfg
mv ./UpgradeFile.bin ./DSN4715/1001/1000/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/1001/1000/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-1001-1001.cfg
./GenerateOTAUpgImage GenerateUpgImage-1001-1001.cfg
mv ./UpgradeFile.bin ./DSN4715/1001/1001/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/1001/1001/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-65535-65535.cfg
./GenerateOTAUpgImage GenerateUpgImage-65535-65535.cfg
mv ./UpgradeFile.bin ./DSN4715/65535/65535/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/65535/65535/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-ddb-crc.cfg
./GenerateOTAUpgImage GenerateUpgImage-ddb-crc.cfg
mv ./UpgradeFile.bin ./DSN4715/ddb_crc/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/ddb_crc/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-dii-crc.cfg
./GenerateOTAUpgImage GenerateUpgImage-dii-crc.cfg
mv ./UpgradeFile.bin ./DSN4715/dii_crc/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/dii_crc/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-downloadheader-crc.cfg
./GenerateOTAUpgImage GenerateUpgImage-downloadheader-crc.cfg
mv ./UpgradeFile.bin ./DSN4715/downloadheader_crc/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/downloadheader_crc/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-downloadpid-1030-tableid-1.cfg
./GenerateOTAUpgImage GenerateUpgImage-downloadpid-1030-tableid-1.cfg
mv ./UpgradeFile.bin ./DSN4715/downloadpid_1030_tableid_0/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/downloadpid_1030_tableid_0/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-dsi-crc.cfg
./GenerateOTAUpgImage GenerateUpgImage-dsi-crc.cfg
mv ./UpgradeFile.bin ./DSN4715/dsi_crc/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/dsi_crc/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-incorrect-hardver.cfg
./GenerateOTAUpgImage GenerateUpgImage-incorrect-hardver.cfg
mv ./UpgradeFile.bin ./DSN4715/incorrect_hardware/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/incorrect_hardware/UpgradeFile.ts


./GenerateUSBUpgImage GenerateUpgImage-incorrect-machinedes.cfg
./GenerateOTAUpgImage GenerateUpgImage-incorrect-machinedes.cfg
mv ./UpgradeFile.bin ./DSN4715/incorrect_machinedes/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/incorrect_machinedes/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-incorrect-manufacturedes.cfg
./GenerateOTAUpgImage GenerateUpgImage-incorrect-manufacturedes.cfg
mv ./UpgradeFile.bin ./DSN4715/incorrect_manuf/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/incorrect_manuf/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-incorrect-oui.cfg
./GenerateOTAUpgImage GenerateUpgImage-incorrect-oui.cfg
mv ./UpgradeFile.bin ./DSN4715/incorrect_oui/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/incorrect_oui/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1100.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1100.cfg
mv ./UpgradeFile.bin ./DSN4715/portion/1100/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/portion/1100/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1101.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1101.cfg
mv ./UpgradeFile.bin ./DSN4715/portion/1101/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/portion/1101/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1102.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1102.cfg
mv ./UpgradeFile.bin ./DSN4715/portion/1102/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/portion/1102/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1103.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1103.cfg
mv ./UpgradeFile.bin ./DSN4715/portion/1103/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/portion/1103/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1104.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1104.cfg
mv ./UpgradeFile.bin ./DSN4715/portion/1104/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/portion/1104/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1200.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1200.cfg
mv ./UpgradeFile.bin ./DSN4715/bootlogo_white/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/bootlogo_white/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1201.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1201.cfg
mv ./UpgradeFile.bin ./DSN4715/bootlogo_black_no_progress/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/bootlogo_black_no_progress/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1202.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1202.cfg
mv ./UpgradeFile.bin ./DSN4715/loader_resource_white/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/loader_resource_white/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1203.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1203.cfg
mv ./UpgradeFile.bin ./DSN4715/loader_resource_black/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/loader_resource_black/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1204.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1204.cfg
mv ./UpgradeFile.bin ./DSN4715/boot_err_code/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/boot_err_code/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-specil-1205.cfg
./GenerateOTAUpgImage GenerateUpgImage-specil-1205.cfg
mv ./UpgradeFile.bin ./DSN4715/loader_err_code/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/loader_err_code/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-wrong-signed.cfg
./GenerateOTAUpgImage GenerateUpgImage-wrong-signed.cfg
mv ./UpgradeFile.bin ./DSN4715/wrong_signed/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/wrong_signed/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-big.cfg
./GenerateOTAUpgImage GenerateUpgImage-big.cfg
mv ./UpgradeFile.bin ./DSN4715/big_size/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/big_size/UpgradeFile.ts

./GenerateUSBUpgImage GenerateUpgImage-excessive-big.cfg
./GenerateOTAUpgImage GenerateUpgImage-excessive-big.cfg
mv ./UpgradeFile.bin ./DSN4715/excessive_big_size/UpgradeFile.bin
mv ./UpgradeFile.ts ./DSN4715/excessive_big_size/UpgradeFile.ts