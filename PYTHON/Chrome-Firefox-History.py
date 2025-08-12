import os, shutil, sqlite3, tempfile, openpyxl
from datetime import datetime, timedelta, timezone
from tabulate import tabulate
from colorama import init, Fore
init(autoreset=True)

def ffx_time(t): return datetime.fromtimestamp(t/1e6, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S') if t else "No Data"
def chr_time(t): return (datetime(1601, 1, 1) + timedelta(microseconds=t)).replace(tzinfo=timezone.utc).strftime('%Y-%m-%d %H:%M:%S') if t else "No Data"
def ffx_path(): return os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Mozilla", "Firefox", "Profiles")
def chr_path(): return os.path.join(os.path.expanduser("~"), "AppData", "Local", "Google", "Chrome", "User Data")
def cp_db(p): 
    try:
        t = os.path.join(tempfile.gettempdir(), f"History_copy_{os.getpid()}")
        shutil.copy2(p, t)
        return t
    except Exception as e:
        print(Fore.RED + f"Error copying Chrome DB: {e}")
        return None

ffx_q = """SELECT p.url, p.title, MIN(hv.visit_date), MAX(hv.visit_date), COUNT(hv.id)
FROM moz_places p JOIN moz_historyvisits hv ON p.id = hv.place_id
GROUP BY p.url, p.title ORDER BY MAX(hv.visit_date) DESC;"""

chr_q = """SELECT urls.url, urls.title, visits.visit_time
FROM urls, visits WHERE urls.id = visits.url ORDER BY visits.visit_time DESC;"""

def get_ffx():
    p, data = ffx_path(), {}
    print(Fore.BLUE + f"Fetching Firefox history from: {p}")
    if not os.path.exists(p): print(Fore.RED + f"Not found: {p}"); return data
    for prof in [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))]:
        db = os.path.join(p, prof, "places.sqlite")
        if not os.path.exists(db): print(Fore.YELLOW + f"Missing: {prof}"); continue
        try:
            c = sqlite3.connect(db).cursor(); c.execute(ffx_q)
            rows = c.fetchall(); c.connection.close()
            if rows: data[prof] = rows
        except Exception as e: print(Fore.RED + f"Error in {prof}: {e}")
    return data

def get_chr():
    p, data = chr_path(), {}
    print(Fore.BLUE + f"\nFetching Chrome history from: {p}")
    if not os.path.exists(p): print(Fore.RED + f"Not found: {p}"); return data
    for prof in [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))]:
        db = os.path.join(p, prof, "History")
        if not os.path.exists(db): print(Fore.YELLOW + f"Missing: {prof}"); continue
        temp = cp_db(db) or db
        try:
            c = sqlite3.connect(temp).cursor(); c.execute(chr_q)
            rows = c.fetchall(); c.connection.close()
            if temp != db: os.remove(temp)
            if rows: data[prof] = rows
        except Exception as e:
            print(Fore.RED + f"Error in {prof}: {e}")
            if temp != db:
                try: os.remove(temp)
                except: pass
    return data

def to_excel(ffx, chr, out="Browser_History.xlsx"):
    print(Fore.BLUE + "\nSaving all history to Excel...")
    wb = openpyxl.Workbook(); wb.remove(wb.active)
    for prof, rows in ffx.items():
        name = f"firefox_{prof}"[:31]; ws = wb.create_sheet(title=name)
        ws.append(["URL", "Title", "First Visit (UTC)", "Last Visit (UTC)", "Visit Count"])
        for u, t, f, l, c in rows: ws.append([u, t, ffx_time(f), ffx_time(l), c])
    for prof, rows in chr.items():
        name = f"chrome_{prof}"[:31]; ws = wb.create_sheet(title=name)
        ws.append(["URL", "Title", "Visit Time (UTC)"])
        for u, t, v in rows: ws.append([u, t, chr_time(v)])
    wb.save(out)
    print(Fore.GREEN + f"Saved to {out}")

def summary(ffx, chr):
    print(Fore.BLUE + "\nSummary:")
    print(Fore.CYAN + "Firefox:")
    for p, r in ffx.items(): print(f"  {p}: {len(r)} entries")
    print(Fore.CYAN + "\nChrome:")
    for p, r in chr.items(): print(f"  {p}: {len(r)} entries")

def main():
    f, c = get_ffx(), get_chr()
    to_excel(f, c)
    summary(f, c)

if __name__ == "__main__": main()
