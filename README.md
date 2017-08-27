# Auto_Backup_Script

資料庫自動備份

Linux設定說名在Terminal環境上
輸入**crontab -e** 進入使用者設定工作排程模式
輸入 預設定參數後保存離開

    分 時 日期 月份 週 指令
    
ex: 
    0 8 * * 5 python /home/user/backup/backup.py


MySQL參考資料
1. Q -> Warning: Using a password on the command line interface can be insecure
   
   A -> https://shazi.info/mysql-%E5%9F%B7%E8%A1%8C-bash-script-%E5%87%BA%E7%8F%BE-warning-using-a-password-on-the-command-line-interface-can-be-insecure/
