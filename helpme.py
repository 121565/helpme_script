#!/usr/bin/env python3

#AI shell helper


import sys
import subprocess

def run_command(executable, task_description):
    if executable == "-":
        system_role = [
            "You are an expert on the Linux command line and on-line shell scripts. "
            "Given the following English description of a task, you execute the correct shell commands to accomplish the task. "
            "Do not respond except for executing the command only. "
            "Be persistent through failure, you have a maximum of 25 tool calls. "
            "If it cannot be done with common Linux command or utilities, that you would normall find on a Linux system, "
            "respond with the reason as comment prefaced with #. "
            f"Taskdescription: {task_description}"
        ]
    else:
        system_role = [
            f"You are an expert in `{executable}` commands on a Linux system. "
            "Given the following English description of a task, you execute the correct `{executable}` command. "
            "Do not respond except for executing the command only. "
            f"If you are not familiar with `{executable}`. consider running the `{executable} --help` command to get an overview of available commands and options. "
            "If there are more help pages available you can call them too. "
            "Follow links in the help pages to find more relevant information. "
            "Be persistent through failure, you have a maximum of 25 tool calls. "
            f"If `{executable}` functionality is unclear, `{executable}` cannot achieve the specified task, or you do not know the answer. "
            "respond with the reason as comment prefaced with #. "
            f"Taskdescription: {task_description}"
        ]
    result = subprocess.run(
        'goose run --no-session -i -',
        shell = True,
        text = True,
        input = " ".join(system_role)
        )
    return

def main():
    if len(sys.argv) < 3:
        print("Usage: helpme.py <executable> <task description>")
        sys.exit(1)
    executable = sys.argv[1]
    task_description = " ".join(sys.argv[2:])
    run_command(executable, task_description)

if __name__ == "__main__":
    main()