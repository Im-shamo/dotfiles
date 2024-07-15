function sudotime --wraps='sudo -E timeshift-gtk' --description 'alias sudotime sudo -E timeshift-gtk'
  sudo -E timeshift-gtk $argv
        
end
