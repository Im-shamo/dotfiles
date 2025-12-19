function update_keepassxc --wraps="rclone copy ~/Documents/Keepassxc/ 'Google Drive':Keepassxc" --description "Uploads keepassxc to Google Drive"
    rclone copy ~/Documents/Keepassxc/ 'Google Drive':Keepassxc $argv
end
