if [[ -e /usr/share/cachyos-zsh-config/cachyos-config.zsh ]]; then
    source /usr/share/cachyos-zsh-config/cachyos-config.zsh
fi

POWERLEVEL9K_INSTANT_PROMPT=off
POWERLEVEL9K_DISABLE_CONFIGURATION_WIZARD=true

if [[ -e /usr/bin/oh-my-posh ]]; then
    eval "$(oh-my-posh init zsh --config ~/Clone/dotfiles/shamo.omp.jsonc)"
fi
