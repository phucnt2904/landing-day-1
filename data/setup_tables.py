import sqlite3, json, re
from datetime import datetime

DB = r"d:\AI91\landing-day-1\brain.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# ── PRODUCTS ─────────────────────────────────────────────
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    price       INTEGER,                       -- giá bán (VND)
    description TEXT,
    image_url   TEXT,
    stock_status TEXT   DEFAULT 'con_hang',     -- con_hang | het_hang
    posted_at   TEXT,                           -- ngày đăng bán (để tính post >= 1 năm -> hết hàng)
    created_at  TEXT    DEFAULT (datetime('now','localtime')),
    updated_at  TEXT    DEFAULT (datetime('now','localtime'))
)
""")

# ── CUSTOMERS ────────────────────────────────────────────
cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT,
    phone         TEXT,
    instagram     TEXT,
    email         TEXT,
    registered_at TEXT,                          -- thời điểm đăng ký (từ form khảo sát/danh sách chờ)
    source        TEXT    DEFAULT 'khao_sat',    -- khao_sat | dat_hang | thu_cong...
    notes         TEXT,                          -- ghi chú thêm (vd: trả lời khảo sát)
    created_at    TEXT    DEFAULT (datetime('now','localtime')),
    updated_at    TEXT    DEFAULT (datetime('now','localtime')),
    UNIQUE(phone, instagram)
)
""")

# ── ORDERS ───────────────────────────────────────────────
cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id  INTEGER NOT NULL REFERENCES customers(id),
    product_id   INTEGER REFERENCES products(id),
    product_name TEXT,                          -- lưu tên sp tại thời điểm mua (phòng khi sp đổi/xoá)
    amount       INTEGER,                       -- tổng tiền (VND)
    status       TEXT    DEFAULT 'cho_xu_ly',   -- cho_xu_ly | da_dat_coc | da_thanh_toan | dang_ship | hoan_thanh | huy
    order_date   TEXT    DEFAULT (datetime('now','localtime')),
    notes        TEXT,
    created_at   TEXT    DEFAULT (datetime('now','localtime')),
    updated_at   TEXT    DEFAULT (datetime('now','localtime'))
)
""")

conn.commit()

# ── IMPORT CUSTOMERS FROM "Khảo sát" SHEET ──────────────────
with open(r"d:\AI91\landing-day-1\data\waitlist.json", 'r', encoding='utf-8') as f:
    sheets = json.load(f)

rows = sheets["Khảo sát"][1:]  # skip header

inserted, skipped = 0, 0
for row in rows:
    stt, thoi_gian, ten, sdt, instagram, email = row[0], row[1], row[2], row[3], row[4], row[5]
    da_tung, biet_qua, san_pham, can_tro, muc_gia = row[6], row[7], row[8], row[9], row[10]

    # format phone: stored as float (leading 0 stripped) -> 10-digit string
    phone = None
    if sdt is not None:
        phone = str(int(sdt))
        if len(phone) == 9:
            phone = "0" + phone

    # parse "HH:MM:SS D/M/YYYY" -> ISO datetime
    registered_at = thoi_gian
    try:
        dt = datetime.strptime(thoi_gian, "%H:%M:%S %d/%m/%Y")
        registered_at = dt.strftime("%Y-%m-%dT%H:%M:%S")
    except (ValueError, TypeError):
        pass

    notes_parts = []
    if da_tung: notes_parts.append(f"Đã từng order Taobao: {da_tung}")
    if biet_qua: notes_parts.append(f"Biết Nomie qua: {biet_qua}")
    if san_pham: notes_parts.append(f"Sản phẩm quan tâm: {san_pham}")
    if can_tro: notes_parts.append(f"Lý do cản bước: {can_tro}")
    if muc_gia: notes_parts.append(f"Mức giá thường chi: {muc_gia}")
    notes = " | ".join(notes_parts)

    try:
        cur.execute("""
            INSERT INTO customers (name, phone, instagram, email, registered_at, source, notes)
            VALUES (?, ?, ?, ?, ?, 'khao_sat', ?)
        """, (ten, phone, instagram, email, registered_at, notes))
        inserted += 1
    except sqlite3.IntegrityError:
        skipped += 1

conn.commit()
print(f"Inserted {inserted} customers, skipped {skipped} duplicates")

cur.execute("SELECT COUNT(*) FROM customers")
print("Total customers:", cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM products")
print("Total products:", cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM orders")
print("Total orders:", cur.fetchone()[0])

conn.close()
