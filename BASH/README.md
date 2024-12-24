# Welcome to BASH Sripting

## BASH Sripting Resources:

| **S.N** | **Resource**                                                                 |
|---------|-------------------------------------------------------------------------------|
| 1       | [Devhints - Bash](https://devhints.io/bash)                                   |
| 2       | [Awesome Cheatsheets - Bash](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh) |
| 3       | [Bash Cheat Sheet - RehanSaeed](https://github.com/RehanSaeed/Bash-Cheat-Sheet) |
| 4       | [Zero2DevOps - Bash Scripting Cheat Sheet](https://www.zero2devops.com/blog/bash-scripting-cheat-sheet) |


---



# 100 Bash Scripting Hacks for Hackers and Security Professionals

## 0. **While Loop**
For loo
```bash
while read url; do
echo "Running at :" "$url"
done <parameters/param.txt
```


## 00. **For loo**

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

