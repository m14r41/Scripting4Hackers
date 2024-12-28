## Sample Output

![image](https://github.com/user-attachments/assets/33f66918-892d-46ed-bb03-d21b2ae15170)


For clarification on how the script handles the **start time** and **end time** when you run the script. Let me break it down for you:

### 1. **Start Date Time**:
   - **What is asked**: When you run the script, it will prompt you for a **start date** (the first date of the range). 
   - If you provide a date in the **YYYY-MM-DD** format, it will use that specific **start date** at midnight (00:00:00 hours). 
     - Example: If you input `2024-12-15`, it will consider the start date as **2024-12-15 00:00:00** (midnight of that date).
   - **Default behavior**: If you leave the start date blank, it will default to **14 days ago** from the current date and time, but **at midnight** of that day.
     - For example: If today is **2024-12-28**, and you don't provide a start date, the script will use **2024-12-14 00:00:00**.

### 2. **End Date Time**:
   - **What is asked**: The script will also prompt you for an **end date** (the last date of the range).
   - If you provide a date in **YYYY-MM-DD** format, it will use that specific **end date** at midnight (00:00:00 hours) by default, and consider builds up to that date **before** the midnight of that day.
     - Example: If you input `2024-12-20`, the end time will be **2024-12-20 00:00:00**, meaning it will include builds **up until** midnight on December 20th, 2024.
   - **Default behavior**: If you leave the end date blank, it will default to the **current date and time** you are running the script.
     - Example: If you run the script on **2024-12-28 at 14:30:00**, the end date will be set to **2024-12-28 14:30:00** (the current moment).

### To summarize:
1. **Start Date**: 
   - If a specific date is provided, it will use that date at **midnight (00:00:00)**.
   - If left blank, it defaults to **14 days ago** at midnight of that day.

2. **End Date**: 
   - If a specific date is provided, it will use that date at **midnight (00:00:00)**.
   - If left blank, it defaults to **the current date and time** you run the script.

### Example:
Let's say today is **2024-12-28** and you run the script.

- **If you provide a start date of 2024-12-15**:
  - The **start date** will be **2024-12-15 00:00:00** (midnight of December 15th).
- **If you provide an end date of 2024-12-20**:
  - The **end date** will be **2024-12-20 00:00:00** (midnight of December 20th).

- **If you leave both the start and end dates blank**:
  - The **start date** will default to **2024-12-14 00:00:00** (14 days ago from today).
  - The **end date** will default to **2024-12-28 14:30:00** (the current moment you run the script).

---

