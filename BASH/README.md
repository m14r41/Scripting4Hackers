# Welcome to BASH Sripting

## List of BASH Project

| S.N | Project Name | Description |
|-----|--------------|-------------|
| 1   | [Configure Static-IP in VirtualMachine](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/Configure%20Static-IP%20in%20VirtualMachine) | Set up a static IP for a Virtual Machine |
| 2   | [Contribute to someone else's repository](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/Contribute%20to%20someone%20else's%20repository) | Contributed to another repository |
| 3   | [Create new repository on the command line](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/Create%20new%20repository%20on%20the%20command%20line) | Created a new Git repository via the command line |
| 4   | [Delete Github Repository Without Losing Stars and Forks](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/Delete%20Github%20Repository%20Without%20Losing%20Stars%20and%20Forks) | Updated message for deleting repositories |
| 5   | [GREP and SED](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/GREP%20and%20SED) | Demonstrated usage of `grep` and `sed` tools |
| 6   | [Push GitHub Repo by CMD](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/Push%20GitHub%20Repo%20by%20CMD) | Pushed a repository to GitHub using the command line |
| 7   | [Semgrep Code Review Scan](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/Semgrep%20Code%20Review%20Scan) | Used Semgrep for code review scanning |
| 8   | [Simple Screen Recorder](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/Simple%20Screen%20Recorder) | Created a simple screen recording tool |
| 9   | [ZSH Fix Issue](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/ZSH%20Fix%20Issue) | Fixed issues related to ZSH shell |
| 10  | [Miscellaneous](https://github.com/m14r41/Scripting4Hackers/tree/main/BASH/tools) | Added various tools for development |



### BASH Scripting Resources:

| **S.N** | **Resource**                                                                 | **Description**                                                                                     | **Credit**                      |
|---------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------|
| 1       | [Devhints - Bash](https://devhints.io/bash)                                   | Concise and well-structured cheat sheet for Bash commands and scripting.                           | Devhints.io                     |
| 2       | [Awesome Cheatsheets - Bash](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh) | A comprehensive collection of Bash scripting tips and commands.                                    | GitHub/LeCoupa                  |
| 3       | [Bash Cheat Sheet - RehanSaeed](https://github.com/RehanSaeed/Bash-Cheat-Sheet) | Detailed guide covering essential Bash commands and their use cases.                               | GitHub/RehanSaeed               |
| 4       | [Zero2DevOps - Bash Scripting Cheat Sheet](https://www.zero2devops.com/blog/bash-scripting-cheat-sheet) | Practical cheat sheet for Bash scripting tailored for DevOps use cases.                           | Zero2DevOps Blog                |



# Create a Simple Menu

```bash
echo "1. Option 1"
echo "2. Option 2"
echo "3. Option 3"
read -p "Choose an option: " choice
case $choice in
    1) echo "You chose Option 1";;
    2) echo "You chose Option 2";;
    3) echo "You chose Option 3";;
    *) echo "Invalid option";;
esac

```
# Read User Input and stopred

```bash
read -p "Enter input: " variable


```

# Generate Random Numbers in Script

```bash
RANDOM=$$
echo $RANDOM

```
# Echo with Colored Text
```bash
echo -e "\033[31mThis is red text\033[0m"

```


# Basic Colors

```bash
black="\033[30m"  # echo -e "\033[30mBlack\033[0m"
red="\033[31m"    # echo -e "\033[31mRed\033[0m"
green="\033[32m"  # echo -e "\033[32mGreen\033[0m"
yellow="\033[33m" # echo -e "\033[33mYellow\033[0m"
blue="\033[34m"   # echo -e "\033[34mBlue\033[0m"
magenta="\033[35m" # echo -e "\033[35mMagenta\033[0m"
cyan="\033[36m"   # echo -e "\033[36mCyan\033[0m"
white="\033[37m"  # echo -e "\033[37mWhite\033[0m"

# Bold Colors
bold_black="\033[1;30m"  # echo -e "\033[1;30mBold Black\033[0m"
bold_red="\033[1;31m"    # echo -e "\033[1;31mBold Red\033[0m"
bold_green="\033[1;32m"  # echo -e "\033[1;32mBold Green\033[0m"
bold_yellow="\033[1;33m" # echo -e "\033[1;33mBold Yellow\033[0m"
bold_blue="\033[1;34m"   # echo -e "\033[1;34mBold Blue\033[0m"
bold_magenta="\033[1;35m" # echo -e "\033[1;35mBold Magenta\033[0m"
bold_cyan="\033[1;36m"   # echo -e "\033[1;36mBold Cyan\033[0m"
bold_white="\033[1;37m"  # echo -e "\033[1;37mBold White\033[0m"

# Background Colors
bg_black="\033[40m"   # echo -e "\033[40mBlack Background\033[0m"
bg_red="\033[41m"     # echo -e "\033[41mRed Background\033[0m"
bg_green="\033[42m"   # echo -e "\033[42mGreen Background\033[0m"
bg_yellow="\033[43m"  # echo -e "\033[43mYellow Background\033[0m"
bg_blue="\033[44m"    # echo -e "\033[44mBlue Background\033[0m"
bg_magenta="\033[45m" # echo -e "\033[45mMagenta Background\033[0m"
bg_cyan="\033[46m"    # echo -e "\033[46mCyan Background\033[0m"
bg_white="\033[47m"   # echo -e "\033[47mWhite Background\033[0m"

# Reset color
reset="\033[0m"       # echo -e "\033[0mReset Color\033[0m"

# Printing colors with their variables
echo -e "${black}Black${reset}"
echo -e "${red}Red${reset}"
echo -e "${green}Green${reset}"
echo -e "${yellow}Yellow${reset}"
echo -e "${blue}Blue${reset}"
echo -e "${magenta}Magenta${reset}"
echo -e "${cyan}Cyan${reset}"
echo -e "${white}White${reset}"

echo -e "${bold_black}Bold Black${reset}"
echo -e "${bold_red}Bold Red${reset}"
echo -e "${bold_green}Bold Green${reset}"
echo -e "${bold_yellow}Bold Yellow${reset}"
echo -e "${bold_blue}Bold Blue${reset}"
echo -e "${bold_magenta}Bold Magenta${reset}"
echo -e "${bold_cyan}Bold Cyan${reset}"
echo -e "${bold_white}Bold White${reset}"

echo -e "${bg_black}Black Background${reset}"
echo -e "${bg_red}Red Background${reset}"
echo -e "${bg_green}Green Background${reset}"
echo -e "${bg_yellow}Yellow Background${reset}"
echo -e "${bg_blue}Blue Background${reset}"
echo -e "${bg_magenta}Magenta Background${reset}"
echo -e "${bg_cyan}Cyan Background${reset}"
echo -e "${bg_white}White Background${reset}"

```


# 100 Bash Scripting Hacks for Hackers and Security Professionals

## 0. **While Loop**
For loo
```bash
while read url; do
echo "Running at :" "$url"
done <parameters/param.txt
```


## 1. **For loop**

```bash
for word in $(cat parameters/param.txt); do echo "$word"; done
```

```markdown
# Top 100 Bash Scripting Concepts

## 1. **While Loop**
```bash
while read url; do
  echo "Running at :" "$url"
done < parameters/param.txt
```

## 2. **For Loop**
```bash
for word in $(cat parameters/param.txt); do
  echo "$word"
done
```

## 3. **If-Else Statement**
```bash
if [ "$var" -eq 1 ]; then
  echo "Variable is 1"
else
  echo "Variable is not 1"
fi
```

## 4. **Case Statement**
```bash
case "$variable" in
  "option1") echo "Option 1";;
  "option2") echo "Option 2";;
  *) echo "Other option";;
esac
```

## 5. **Functions**
```bash
my_function() {
  echo "This is a function"
}

my_function
```

## 6. **Reading User Input**
```bash
read -p "Enter your name: " name
echo "Hello, $name!"
```

## 7. **Arrays**
```bash
arr=("apple" "banana" "cherry")
echo ${arr[0]}   # Output: apple
```

## 8. **Redirecting Output**
```bash
echo "This is a test" > output.txt
cat output.txt
```

## 9. **Pipes**
```bash
cat file.txt | grep "search term" | sort
```

## 10. **Variables**
```bash
name="John"
echo "Hello, $name!"
```

## 11. **Arithmetic Operations**
```bash
a=10
b=20
sum=$((a + b))
echo "Sum: $sum"
```

## 12. **String Length**
```bash
str="Hello, World"
echo ${#str}   # Output: 13
```

## 13. **Substring Extraction**
```bash
str="Hello, World"
echo ${str:7:5}  # Output: World
```

## 14. **String Comparison**
```bash
str1="Hello"
str2="Hello"
if [ "$str1" == "$str2" ]; then
  echo "Strings are equal"
fi
```

## 15. **Command Substitution**
```bash
current_date=$(date)
echo "Current Date: $current_date"
```

## 16. **Exit Status**
```bash
command
if [ $? -eq 0 ]; then
  echo "Command succeeded"
else
  echo "Command failed"
fi
```

## 17. **Wildcards**
```bash
echo *.txt    # List all .txt files
```

## 18. **Getting Script Arguments**
```bash
echo "First argument: $1"
echo "Second argument: $2"
```

## 19. **File Test Operators**
```bash
if [ -f "file.txt" ]; then
  echo "File exists"
else
  echo "File does not exist"
fi
```

## 20. **Redirection Operators**
```bash
echo "This is an error" >&2  # Redirect to stderr
```

## 21. **Background Process**
```bash
command &    # Run command in background
```

## 22. **Foreground Process**
```bash
command     # Run command in foreground
```

## 23. **Killing a Process**
```bash
kill $(pidof process_name)
```

## 24. **Loop Control**
```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    continue
  fi
  echo $i
done
```

## 25. **Break Statement**
```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    break
  fi
  echo $i
done
```

## 26. **Logging to a File**
```bash
echo "Error occurred" >> error_log.txt
```

## 27. **File Permissions**
```bash
chmod +x script.sh   # Make script executable
```

## 28. **Reading a File Line by Line**
```bash
while IFS= read -r line; do
  echo "$line"
done < file.txt
```

## 29. **File Copying**
```bash
cp source.txt destination.txt
```

## 30. **File Moving**
```bash
mv source.txt destination.txt
```

## 31. **File Deleting**
```bash
rm file.txt
```

## 32. **Directory Creation**
```bash
mkdir new_directory
```

## 33. **Changing Directory**
```bash
cd /path/to/directory
```

## 34. **Listing Directory Contents**
```bash
ls -l
```

## 35. **Finding Files**
```bash
find /path -name "file.txt"
```

## 36. **Testing Command Success**
```bash
if command; then
  echo "Command succeeded"
fi
```

## 37. **Command Line Arguments (shift)**
```bash
echo "First Argument: $1"
shift
echo "Second Argument: $1"
```

## 38. **Get Current User**
```bash
echo $USER
```

## 39. **Get Current Directory**
```bash
pwd
```

## 40. **Using Exit Codes**
```bash
exit 1   # Exits script with status code 1
```

## 41. **Get File Metadata**
```bash
stat file.txt
```

## 42. **Process ID**
```bash
echo $$
```

## 43. **Cron Jobs**
```bash
crontab -e   # Edit cron jobs
```

## 44. **Creating a Tar Archive**
```bash
tar -cvf archive.tar directory/
```

## 45. **Extracting a Tar Archive**
```bash
tar -xvf archive.tar
```

## 46. **Using Sudo**
```bash
sudo command
```

## 47. **Background Process with nohup**
```bash
nohup command &
```

## 48. **Wait for Process to Complete**
```bash
wait $!   # Wait for the last background job to finish
```

## 49. **Setting Variables from Files**
```bash
source file.sh
```

## 50. **Date Formatting**
```bash
date "+%Y-%m-%d"
```

## 51. **Creating an Empty File**
```bash
touch newfile.txt
```

## 52. **Viewing the Last N Lines of a File**
```bash
tail -n 10 file.txt
```

## 53. **Viewing the First N Lines of a File**
```bash
head -n 10 file.txt
```

## 54. **Searching for a Pattern in a File**
```bash
grep "pattern" file.txt
```

## 55. **Replacing Text in a File**
```bash
sed -i 's/old/new/g' file.txt
```

## 56. **Cutting Columns in a File**
```bash
cut -d, -f1 file.csv
```

## 57. **Sorting File Contents**
```bash
sort file.txt
```

## 58. **Counting Lines in a File**
```bash
wc -l file.txt
```

## 59. **Removing Duplicate Lines in a File**
```bash
sort file.txt | uniq
```

## 60. **Finding Files with Specific Permissions**
```bash
find /path -perm 644
```

## 61. **Show Active Network Connections**
```bash
netstat -tuln
```

## 62. **Disk Usage**
```bash
du -sh /path/to/directory
```

## 63. **Checking Free Disk Space**
```bash
df -h
```

## 64. **Monitoring Processes**
```bash
top
```

## 65. **Displaying Process Info**
```bash
ps aux
```

## 66. **Killing a Process by Name**
```bash
pkill process_name
```

## 67. **Searching System Logs**
```bash
grep "error" /var/log/syslog
```

## 68. **Checking Available Memory**
```bash
free -h
```

## 69. **Checking Network Interfaces**
```bash
ifconfig
```

## 70. **Change Ownership of a File**
```bash
chown user:group file.txt
```

## 71. **Change Group of a File**
```bash
chgrp group file.txt
```

## 72. **Setting File Access Permissions**
```bash
chmod 755 file.txt
```

## 73. **Changing File Modification Time**
```bash
touch -t 202112010000 file.txt
```

## 74. **Set an Alias**
```bash
alias ll='ls -al'
```

## 75. **Unalias**
```bash
unalias ll
```

## 76. **Display Network Route**
```bash
route -n
```

## 77. **Save Output of a Command to a File**
```bash
command > output.txt
```

## 78. **Append Output to a File**
```bash
command >> output.txt
```

## 79. **Set Up a Simple HTTP Server**
```bash
python3 -m http.server
```

## 80. **Test Connection to a Remote Server**
```bash
ping -c 4 remote_server.com
```

## 81. **Start a Bash Script in the Background**
```bash
./script.sh &
```

## 82. **Logging Output to File with Timestamp**
```bash
echo "$(date): $message" >> log.txt
```

## 83. **Check File Type**
```bash
file filename
```

## 84. **Monitor File Changes in Real-Time**
```bash
tail -f file.txt
```

## 85. **Create a Symbolic Link**
```bash
ln -s target_file link_name
```

## 86. **Create a Hard Link**
```bash
ln target_file link_name
```

## 87. **Check if a Directory Exists**
```bash
if [ -d "dir_name" ]; then
  echo "Directory exists"
fi
```

## 88. **Check if a File Exists**
```bash
if [ -f "file.txt" ]; then
  echo "File exists"
fi
```

## 89. **Validate an IP Address**
```bash
if [[ "$ip" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Valid

 IP"
else
  echo "Invalid IP"
fi
```

## 90. **Check for Specific User**
```bash
id username
```

## 91. **Find Files Larger Than a Specific Size**
```bash
find /path -size +100M
```

## 92. **Get Current Timestamp**
```bash
date +%s
```

## 93. **Check Available Swap Space**
```bash
swapon -s
```

## 94. **Change File Permissions Recursively**
```bash
chmod -R 755 directory/
```

## 95. **Check System Uptime**
```bash
uptime
```

## 96. **Find Processes by Name**
```bash
ps aux | grep process_name
```

## 97. **Count Files in Directory**
```bash
find /path/to/dir -type f | wc -l
```

## 98. **Search Files Containing a Pattern**
```bash
grep -rl "pattern" /path/to/dir
```

## 99. **Run Command in Subshell**
```bash
(command)
```

## 100. **Check Active Services**
```bash
systemctl list-units --type=service
```
```

