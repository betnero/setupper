#!/bin/bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Variables for GitHub aliases and wallpaper
ALIASES_REPO="https://raw.githubusercontent.com/betnero/sobriquet/main/aliases.txt"
WALLPAPER_PATH="$HOME/Desktop/dark-wallpaper.jpg"

# Function to check command existence
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Detecting the Linux Distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$ID
        VERSION=$VERSION_ID
    elif type lsb_release >/dev/null 2>&1; then
        DISTRO=$(lsb_release -si)
        VERSION=$(lsb_release -sr)
    else
        echo -e "${RED}Unable to determine the Linux distribution.${NC}"
        exit 1
    fi

    echo -e "${YELLOW}Detected Distro: $DISTRO, Version: $VERSION${NC}"
}

# Updating and Upgrading Packages Based on Distribution
update_and_upgrade() {
    case "$DISTRO" in
        debian|ubuntu)
            sudo apt update && sudo apt upgrade -y
            ;;
        arch)
            sudo pacman -Syyu --noconfirm
            ;;
        rhel|centos|fedora)
            if [ "$DISTRO" == "rhel" ] || [ "$VERSION_ID" -ge 8 ]; then
                sudo dnf update -y
            else
                sudo yum update -y
            fi
            ;;
        *)
            echo -e "${RED}Unsupported distribution: $DISTRO${NC}"
            exit 1
            ;;
    esac

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}System updated and upgraded successfully.${NC}"
    else
        echo -e "${RED}Failed to update or upgrade the system.${NC}"
        exit 1
    fi
}

# Installing Packages Based on Distribution
install_package() {
    local package=$1
    case "$DISTRO" in
        debian|ubuntu)
            sudo apt install -y "$package"
            ;;
        arch)
            sudo pacman -S --noconfirm "$package"
            ;;
        rhel|centos|fedora)
            if [ "$DISTRO" == "rhel" ] || [ "$VERSION_ID" -ge 8 ]; then
                sudo dnf install -y "$package"
            else
                sudo yum install -y "$package"
            fi
            ;;
    esac
}

# Install Required Packages
install_packages() {
    declare -a packages=("git" "firefox" "docker.io" "virtualbox" "code" "terminator")
    
    for package in "${packages[@]}"; do
        echo -e "${YELLOW}Installing $package...${NC}"
        install_package "$package"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}$package installed successfully.${NC}"
        else
            echo -e "${RED}Failed to install $package.${NC}"
            exit 1
        fi
    done

    # Docker service enable and start
    sudo systemctl enable docker && sudo systemctl start docker
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Docker started successfully.${NC}"
    else
        echo -e "${RED}Failed to start Docker.${NC}"
        exit 1
    fi
}

# Download and install aliases
install_aliases() {
    curl -o ~/.bashrc "$ALIASES_REPO" && cat ~/.bashrc | grep -v '^#' > ~/.bash_aliases
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Aliases installed successfully.${NC}"
    else
        echo -e "${RED}Failed to install aliases.${NC}"
        exit 1
    fi
    
    # Source the new aliases file
    source ~/.bashrc
}

# Setup UFW (Uncomplicated Firewall)
setup_firewall() {
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    sudo ufw --force enable

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}UFW firewall configured successfully.${NC}"
    else
        echo -e "${RED}Failed to configure UFW firewall.${NC}"
        exit 1
    fi
}

# Set Desktop Theme and Wallpaper
set_desktop_environment() {
    if command_exists gsettings; then
        # Assuming a GNOME environment for demonstration
        gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}Dark theme applied successfully.${NC}"
        else
            echo -e "${RED}Failed to apply dark theme.${NC}"
            exit 1
        fi

        # Set wallpaper
        gsettings set org.gnome.desktop.background picture-uri "file://$WALLPAPER_PATH"
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}Wallpaper set successfully.${NC}"
        else
            echo -e "${RED}Failed to set wallpaper.${NC}"
            exit 1
        fi
    else
        echo -e "${YELLOW}gsettings command not found. Skipping theme and wallpaper setup.${NC}"
    fi
}

# Install additional apps from YAML file
install_apps_from_yaml() {
    local yaml_file="$HOME/install_apps.yaml"

    if [ ! -f "$yaml_file" ]; then
        echo -e "${RED}Apps YAML file does not exist: $yaml_file${NC}"
        exit 1
    fi

    # Parse the YAML and install packages (requires 'yq')
    while IFS= read -r package; do
        echo -e "${YELLOW}Installing additional app: $package...${NC}"
        install_package "$package"
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}$package installed successfully.${NC}"
        else
            echo -e "${RED}Failed to install $package.${NC}"
            exit 1
        fi
    done < <(yq eval '.apps[]' "$yaml_file")
}

# Main script execution
main() {
    detect_distro
    update_and_upgrade
    install_packages
    install_aliases
    setup_firewall
    set_desktop_environment
    install_apps_from_yaml

    echo -e "${GREEN}Linux distro setup completed successfully.${NC}"
}

main
