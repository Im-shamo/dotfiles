#!/usr/bin/python3
import os.path
import subprocess
import json
import argparse


class Pacman:
    def __init__(self):
        self.args = ["pacman", "--needed", "--noconfirm"]

    def install(self, packages: list) -> subprocess.CompletedProcess:
        command = self.args.copy()
        command.append("-S")
        command.insert(0, "sudo")
        command.extend(packages)
        return subprocess.run(command, capture_output=True, text=True)

    def full_system_sync(self) -> subprocess.CompletedProcess:
        command = self.args.copy()
        command.append("-Syu")
        command.insert(0, "sudo")
        return subprocess.run(command, capture_output=True, text=True)

    @staticmethod
    def check(packages: list[str]) -> list[str]:
        error_packages = []
        for package in packages:
            command = ["pacman", "-Ss", package]
            result = subprocess.run(command, capture_output=True, text=True)
            if not result.stdout:
                error_packages.append(package)
        return error_packages


class Yay:
    def __init__(self):
        self.args = ["yay", "--needed", "--noconfirm"]

    def install(self, packages: list) -> subprocess.CompletedProcess:
        command = self.args.copy()
        command.append("-S")
        command.extend(packages)
        return subprocess.run(command, capture_output=True, text=True)

    @staticmethod
    def check(packages: list[str]) -> list[str]:
        error_packages = []
        for package in packages:
            command = ["yay", "-Ss", package]
            result = subprocess.run(command, capture_output=True, text=True)
            if not result.stdout:
                error_packages.append(package)
        return error_packages


def check_packages(all_packages: dict[str, dict[str, list[list[str]]]]) -> dict[str, dict[str, list[str]]]:
    pacman_result = {}
    aur_result = {}
    for package_group_name, package_group in all_packages.items():
        for name, packages in package_group.items():
            pacman_result[name] = Pacman.check(packages[0])
            aur_result[name] = Yay.check(packages[1])

    return {
        "pacman": pacman_result,
        "aur": aur_result
    }


def install_yay() -> subprocess.CompletedProcess:
    return subprocess.run(["yay_install.sh"], capture_output=True, text=True)


def list_packages(all_packages: dict[str, dict[str, list[list[str]]]], detailed=False) -> None:
    for package_group_name, package_group in all_packages.items():
        print(package_group_name.capitalize())
        for name, packages in package_group.items():
            print(f"  - {name.capitalize()}")
            # TODO: Add Full package info


def remove_groups(all_packages: dict[str, dict[str, list[list[str]]]]) -> dict[str, list[list[str]]]:
    result = {}
    for package_group_name, package_group in all_packages.items():
        for name, packages in package_group.items():
            result[name] = packages
    return result


# TODO: Install interface

parser = argparse.ArgumentParser(prog="Program Installer (Arch)")
parser.add_argument("--all", action="store_true", help="All packages")
parser.add_argument("--group", "-g", nargs="+", help="Select package groups")
parser.add_argument("--add", "-a", nargs="+", help="Select packages")
parser.add_argument("--list", "-l", action="store_true", help="List out packages")
parser.add_argument("--check", "-c", action="store_true", help="Check packages")
parser.add_argument("--verbose", action="store_true", help="Output pacman and yay stdout")
args = parser.parse_args()

with open("package.json", "r") as file:
    all_packages = json.load(file)

if __name__ == "__main__":
    if not os.path.exists("/usr/bin/yay"):
        result = install_yay()
        if args.verbose:
            print(result.stderr)
            print(result.stdout)

    pac = Pacman()
    aur = Yay()

    if args.check:
        result = check_packages(all_packages)
        print(result["pacman"])
        print(result["aur"])

    elif args.list:
        list_packages(all_packages)

    elif args.all:
        pass

    elif args.group:
        for g in args.group:
            print(f"Install group: {g}.")
            for name, packages in all_packages[g].items():
                pac_result = pac.install(packages[0])
                aur_result = aur.install(packages[1])
                if args.verbose:
                    print(pac_result.stderr)
                    print(pac_result.stdout)
                    print(aur_result.stderr)
                    print(aur_result.stdout)

    elif args.add:
        removed_groups = remove_groups(all_packages)
        for p in args.add:
            print(f"Install package: {p}")
            pac_result = pac.install(removed_groups[p][0])
            aur_result = aur.install(removed_groups[p][1])
            if args.verbose:
                print(pac_result.stderr)
                print(pac_result.stdout)
                print(aur_result.stderr)
                print(aur_result.stdout)
