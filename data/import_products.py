# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

DB = r"d:\AI91\landing-day-1\brain.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# add category column if not present
cur.execute("PRAGMA table_info(products)")
cols = [r[1] for r in cur.fetchall()]
if "category" not in cols:
    cur.execute("ALTER TABLE products ADD COLUMN category TEXT")

def iso(d):
    return datetime.strptime(d, "%d/%m/%Y").strftime("%Y-%m-%d")

CUTOFF = datetime.strptime("14/06/2025", "%d/%m/%Y")

def status(d):
    return "con_hang" if datetime.strptime(d, "%d/%m/%Y") >= CUTOFF else "het_hang"

# (category, name, price_or_None, description, link, posted_date)
products = [
  # ── BOTTOM ──────────────────────────────────────────
  ("Bottom", "Shorts bi đầu xu (trắng/nâu)", 285000,
   "Size: S - M - L | Màu: Trắng - Nâu | Giao diện năng động nhưng vẫn cứ là điệu đà",
   "https://www.instagram.com/nomie.order/p/DZY2ek5Gohe/", "10/06/2026"),
  ("Bottom", "Short jeans thêu hoa pastel", 280000,
   "Size: S - 4XL | Màu: Hồng - Trắng | Jeans thêu hoa cùng màu pastel - ngọt mà cưng",
   "https://www.instagram.com/nomie.order/p/DW332tdmjaS/", "08/04/2026"),
  ("Bottom", "Quần Kitty cute", 165000,
   "Size: S - M - L - XL | Màu: Nhiều màu | Quần Kitty cute, phô mai que",
   "https://www.instagram.com/nomie.order/p/DPfuoMcgRde/", "07/10/2025"),
  ("Bottom", "Quần đông (không/có lót nỉ)", 200000,
   "Giá: 200.000đ (không lót nỉ) / 240.000đ (có lót nỉ) | Size: S - M - L - XL - 2XL | Quần không thể thiếu trong tủ đông, có 2 loại lót nỉ và không lót nỉ",
   "https://www.instagram.com/nomie.order/p/DB7j651zsPR/", "04/11/2024"),
  ("Bottom", "Quần nỉ bông", 150000,
   "Size: Size 1 (35-52kg) - Size 2 (52-67kg) | Quần nỉ bông, nhiều kiểu",
   "https://www.instagram.com/nomie.order/p/DB1Zod2zFEQ/", "01/11/2024"),
  ("Bottom", "Quần bông Hello Kitty mùa đông", 180000,
   "Size: M - L - XL - 2XL | Quần bông Hello Kitty mùa đông",
   "https://www.instagram.com/nomie.order/p/DAyxIUgTF6D/", "07/10/2024"),
  ("Bottom", "Chân váy chấm bi lụa nâu xanh", 250000,
   "Size: S - 4XL | Màu: Nâu bi xanh | Chất liệu: Lụa | Mặc lên là thấy có gu liền",
   "https://www.instagram.com/nomie.order/p/DW33GmhGqM9/", "08/04/2026"),
  ("Bottom", "Chân váy thun bèo (Loại 1 và 2)", 230000,
   "Giá: Loại 1: 290.000đ / Loại 2: 230.000đ | Size: S - M - L | Màu: Trắng - Xám - Đen | \"Simple but make it cute\"",
   "https://www.instagram.com/nomie.order/p/DPfrtvJgarO/", "07/10/2025"),

  # ── ĐẦM & SET ───────────────────────────────────────
  ("Đầm & Set", "Váy hoa nhỏ (xanh/hồng)", 230000,
   "Size: S - M - L - XL | Màu: Xanh - Hồng | Vườn hoa mùa hè thu nhỏ trong chiếc váy xinh. Diện dạo phố là thấy nũng nịu",
   "https://www.instagram.com/nomie.order/p/DZPp2V9GqTx/", "06/06/2026"),
  ("Đầm & Set", "Váy halter hoa xanh mùa hè", 330000,
   "Size: S - M - L | Màu: Xanh - Hồng | Mang vibe đậm mùa hè",
   "https://www.instagram.com/nomie.order/p/DXePVaMGjk9/", "23/04/2026"),
  ("Đầm & Set", "Váy bi phối ren + nơ", 340000,
   "Size: S - M - L | Màu: Trắng bi đen | Váy bi phối ren cùng họa tiết nơ tạo điểm nhấn",
   "https://www.instagram.com/nomie.order/p/DXbCOBtmiw9/", "22/04/2026"),
  ("Đầm & Set", "Váy wrap chấm bi trắng đen", 290000,
   "Size: S - M - L | Màu: Trắng bi đen | Muốn nổi bật thì mua ngay",
   "https://www.instagram.com/nomie.order/p/DXbBzyLGqIJ/", "22/04/2026"),
  ("Đầm & Set", "Mini dress corset hồng ruffle", 400000,
   "Size: S - M - L | Màu: Hồng pastel | Pastel mà ngọt ngào",
   "https://www.instagram.com/nomie.order/p/DXbBoffmvdj/", "22/04/2026"),
  ("Đầm & Set", "Váy bi nơ phong cách tiểu thư", 330000,
   "Size: S - M - L | Màu: Trắng bi đen | Vibe tiểu thư đài cát",
   "https://www.instagram.com/nomie.order/p/DXbBKJsmmG-/", "22/04/2026"),
  ("Đầm & Set", "Váy babydoll voan tơ xòe bồng", 360000,
   "Size: S - M - L | Màu: Hồng pastel | Váy hai dây babydoll voan tơ xòe bồng cho các nàng bánh bèo",
   "https://www.instagram.com/nomie.order/p/DXBMGDqGql3/", "12/04/2026"),
  ("Đầm & Set", "Váy liền chấm bi (halter neck)", 335000,
   "Size: S - M - L | Màu: Trắng bi đen | Chấm bi mãi thôi",
   "https://www.instagram.com/nomie.order/p/DXBLwu1mhwG/", "12/04/2026"),
  ("Đầm & Set", "Váy phối ren nâu chấm bi", 430000,
   "Size: S - M - L | Màu: Nâu bi trắng | Váy phối ren siêu phẩm, ren mà không hề sến",
   "https://www.instagram.com/nomie.order/p/DW5KGdvmmIU/", "09/04/2026"),
  ("Đầm & Set", "Váy mùa hè 2026 chấm bi nâu", 320000,
   "Size: S - M - L | Màu: Nâu bi trắng | Đích thị là chiếc váy của mùa hè 2026",
   "https://www.instagram.com/nomie.order/p/DW32IpcmnQw/", "08/04/2026"),
  ("Đầm & Set", "Váy satin hồng bánh bèo nơ ren", 370000,
   "Size: S - M - L | Màu: Hồng pastel | Bánh bèo - váy satin cổ yếm ren thắt nơ bèo",
   "https://www.instagram.com/nomie.order/p/DHBs8y6zrF3/", "11/03/2025"),
  ("Đầm & Set", "Váy trắng gân chân bèo", 280000,
   "Size: S - M - L | Màu: Trắng | Không cần quá cầu kì, nhẹ nhàng mà vẫn nổi bật",
   "https://www.instagram.com/nomie.order/p/DHBtjGKTD0z/", "11/03/2025"),
  ("Đầm & Set", "Váy lụa 2 dây quyến rũ", 320000,
   "Size: S - M - L | Màu: Kem / Trắng ngà | Chất liệu: Lụa | Sexy mà lôi cuốn vô cùng",
   "https://www.instagram.com/nomie.order/p/DXBMi0Fmgxw/", "12/04/2026"),
  ("Đầm & Set", "Đầm lụa 2 dây trễ vai", 350000,
   "Size: S - M - L | Màu: Hồng pastel | Chất liệu: Lụa | Đầm lụa siêu sang cho các tình iu",
   "https://www.instagram.com/nomie.order/p/DW5JikRmtiN/", "09/04/2026"),
  ("Đầm & Set", "Set chấm bi đen trắng (áo+quần)", 350000,
   "Size: S - M - L | Màu: Trắng bi đen | Không đụng hàng luôn",
   "https://www.instagram.com/nomie.order/p/DXBL6q5mhFP/", "12/04/2026"),
  ("Đầm & Set", "Set corset + chân váy ruffle hồng", 430000,
   "Size: S - M - L | Màu: Hồng pastel | Đi date mà mặc bộ này thì quá slay",
   "https://www.instagram.com/nomie.order/p/DW5J1p2GmBB/", "09/04/2026"),
  ("Đầm & Set", "Bộ đồ ngủ pyjama kẻ sọc hot", 210000,
   "Size: S - M - L - XL | Màu: Vàng kẻ sọc gấu | Đang hot hit bên Trung; được khách hỏi nhiều, shop sẽ gửi ảnh thật khi khách thắc mắc",
   "https://www.instagram.com/nomie.order/p/DW32XAEmnDX/", "08/04/2026"),
  ("Đầm & Set", "Set đồ hè Hello Kitty", None,
   "Giá: Liên hệ | Size: Không rõ | Màu: Nâu Kitty | \"Mùa hè đang vẫy gọi\"",
   "https://www.instagram.com/nomie.order/p/DKBeMKTzVyy/", "24/05/2025"),
  ("Đầm & Set", "Set đồ Kitty (áo+shorts denim)", None,
   "Giá: Liên hệ | Size: Không rõ | Màu: Đỏ/Trắng Kitty | Set Kitty hợp người đẹp (đợt lên đơn mới)",
   "https://www.instagram.com/nomie.order/p/DIjCGBhzFWy/", "17/04/2025"),
  ("Đầm & Set", "Set áo sơ mi trắng + corset", 450000,
   "Size: S - M - L | Màu: Trắng - Xanh lục | Set áo sơ mi trắng phối corset xanh quân đội - \"ngầu đét\"",
   "https://www.instagram.com/nomie.order/p/DHBuELpTyaJ/", "11/03/2025"),
  ("Đầm & Set", "Bộ đồ ngủ kẻ sọc hồng", 170000,
   "Size: Không rõ | Màu: Hồng | Set 2 dây + quần short kẻ sọc - \"đồ ngủ mà mặc là có người thức đó\"",
   "https://www.instagram.com/nomie.order/p/DHEEJozTVMp/", "11/03/2025"),
  ("Đầm & Set", "Set lông Hello Kitty", 270000,
   "Size: M - L - XL - 2XL | Chất liệu: Lông/nỉ ấm | Set lông Hello Kitty xinh iu",
   "https://www.instagram.com/nomie.order/p/DBy74SCz349/", "31/10/2024"),
  ("Đầm & Set", "Bikini full set star print", 330000,
   "Size: S - M - L | Màu: Nâu star print | Bikini full set nửa kín nửa hở",
   "https://www.instagram.com/nomie.order/p/DW5KZA2mqnu/", "09/04/2026"),

  # ── GIÀY - DÉP ──────────────────────────────────────
  ("Giày - Dép", "Giày sneaker Hello Kitty hồng", 290000,
   "Size: 35 - 40 | Màu: Hồng | \"Em chỉ mê Hello Kitty mãi thôi\" - sneaker Kitty hồng",
   "https://www.instagram.com/nomie.order/p/DFUvhuMTATo/", "27/01/2025"),
  ("Giày - Dép", "Giày Hello Kitty sporty", 290000,
   "Size: 35 - 40 | Màu: Đen - Hồng - Trắng - Xanh trời | Giày Hello Kitty bản sporty, đính logo Kitty",
   "https://www.instagram.com/nomie.order/p/DHBHJSdz1C_/", "10/03/2025"),
  ("Giày - Dép", "Giày Mary Jane đính sao", 350000,
   "Size: 35 - 36 - 37 - 38 - 39 - 40 | Màu: Xanh - Hồng | \"Bước đi lấp lánh cùng mấy bé Mary Jane đính sao\" - vừa cá tính vừa điệu đà",
   "https://www.instagram.com/nomie.order/p/DZW3TIYmg6J/", "09/06/2026"),
  ("Giày - Dép", "Giày đen Mary Jane (ánh kim)", None,
   "Giá: Liên hệ | Size: Không rõ | Màu: Đen | \"Hông có em này trong tủ giày là một thiếu sót lớn\" - mix với đồ gì cũng xinh",
   "https://www.instagram.com/nomie.order/p/DZIIhxDGrwB/", "03/06/2026"),
  ("Giày - Dép", "Giày balet chấm bi đen", 250000,
   "Size: 35 - 39 | Màu: Đen bi trắng | \"Em giày balet mix gì cũng chinh mấy nàng\"",
   "https://www.instagram.com/nomie.order/p/DXLp1XDGiOV/", "16/04/2026"),
  ("Giày - Dép", "BST sandal bệt - cao gót hè (Summer vibe)", None,
   "Giá: Liên hệ | Size: Đủ size | Màu: Tone pastel | BST sandal/bệt/cao gót tone màu siêu xinh cho mùa hè",
   "https://www.instagram.com/nomie.order/p/DIjCfSDzJ_X/", "17/04/2025"),
  ("Giày - Dép", "Sandal hè - BST nhiều mẫu", None,
   "Giá: Liên hệ | Size: Đủ size | Màu: Nhiều màu | \"Thích em nào inbox cho shop tư vấn nhen\"",
   "https://www.instagram.com/nomie.order/p/DXbAlfRmugK/", "22/04/2026"),
  ("Giày - Dép", "Dép bèo nơ đủ màu", 195000,
   "Size: Đủ size | Màu: Kem - Xanh - Hồng - Vàng | \"Bèo bèo mà phối gì cũng hợp\"",
   "https://www.instagram.com/nomie.order/p/DW33bNfGsG-/", "08/04/2026"),
  ("Giày - Dép", "Dép mule nhiều màu", 310000,
   "Size: 35 - 40 | Màu: Đỏ - Vàng - Hồng hoa - Be - Tím - Xanh mint | \"Dịu khaaaa\" - dép mule tone màu siêu xinh cho mùa hè",
   "https://www.instagram.com/nomie.order/p/DIN_-ETT0Qx/", "09/04/2025"),

  # ── PHỤ KIỆN ────────────────────────────────────────
  ("Phụ kiện", "Túi xách đen mini", None,
   "Giá: Liên hệ | Size: One size | Màu: Đen | \"Toàn túi iu iuu, xink xink hông ạ\"",
   "https://www.instagram.com/nomie.order/p/DZH-7dxGpzl/", "03/06/2026"),
  ("Phụ kiện", "Túi nơ nhiều màu", 170000,
   "Size: One size | Màu: Hồng - Đỏ - Vàng chanh - Trắng - Đen | \"Túi nơ siêu điệu\"",
   "https://www.instagram.com/nomie.order/p/DXbAQ2hGhra/", "22/04/2026"),
  ("Phụ kiện", "Túi tote trong suốt đính plushie", 160000,
   "Size: One size | Màu: Hồng pastel - Xanh pastel | Túi tote trong suốt đính plushie cực xinh (chỉ có túi, không kèm charm)",
   "https://www.instagram.com/nomie.order/p/DPfq9n2ARFi/", "07/10/2025"),
  ("Phụ kiện", "Túi xách nhiều kiểu", 260000,
   "Size: One size | \"Top những chiếc túi nên mua nhất năm\" - tiện lợi",
   "https://www.instagram.com/nomie.order/p/DGwh1N6THf4/", "04/03/2025"),
  ("Phụ kiện", "Túi đựng laptop", 149000,
   "Size: One size | \"Túi siêu vễ thương\" - đựng được cả laptop",
   "https://www.instagram.com/nomie.order/p/DA-MtMpT0eQ/", "11/10/2024"),
  ("Phụ kiện", "Balo Hello Kitty hồng thêu", 230000,
   "Size: One size | Màu: Hồng | Balo Hello Kitty thêu hoa siêu ngọt",
   "https://www.instagram.com/nomie.order/p/DHBEogDz9RR/", "10/03/2025"),
  ("Phụ kiện", "Mũ gấu", 139000,
   "Size: One size | \"Mũ gấu cưng xỉu\"",
   "https://www.instagram.com/nomie.order/p/DGwiH0ZTU2x/", "04/03/2025"),
  ("Phụ kiện", "Mũ gấu (mẫu cũ)", 130000,
   "Size: One size | Mũ gấu xinh xẻo, giá siêu tốt",
   "https://www.instagram.com/nomie.order/p/DCDLNgsTqW0/", "07/11/2024"),

  # ── TOP (ÁO) ────────────────────────────────────────
  ("Top", "Cardigan hồng đính nơ nút", None,
   "Giá: Liên hệ | Size: Không rõ | Màu: Hồng pastel | Cardigan nữ nút nơ phong cách tiểu thư - \"Cardigan đây ạ - xinh hong các nàng ơiii\"",
   "https://www.instagram.com/nomie.order/p/C-1lpHEvqWY/", "19/08/2024"),
  ("Top", "Áo khoác Hello Kitty", 330000,
   "Size: S - M - L - XL | Áo khoác Kitty xink chấn động",
   "https://www.instagram.com/nomie.order/p/DHBC6SMzmBi/", "10/03/2025"),
  ("Top", "Hoodie zip Hello Kitty lót nỉ", 289000,
   "Size: S - M - L - XL - 2XL | Hoodie zip Hello Kitty siêu xinh, có lót nỉ ấm áp",
   "https://www.instagram.com/nomie.order/p/DCvUbP5zFTC/", "24/11/2024"),
  ("Top", "Áo CDG buộc nơ đỏ (Noel)", 259000,
   "Size: S - XL | Màu: Đỏ | Áo CDG buộc nơ đỏ mang vibe Noel cực mạnh",
   "https://www.instagram.com/nomie.order/p/DDJX-0rzXQH/", "04/12/2024"),
  ("Top", "Áo lông gấu", 370000,
   "Size: S - M - L - XL - 2XL | Áo gấu lông siêu ấm cho mùa đông",
   "https://www.instagram.com/nomie.order/p/DCDLHFazwUE/", "07/11/2024"),
  ("Top", "Áo phao bánh bèo", 385000,
   "Size: S - M - L - XL | Bộ sưu tập áo phao cho các nàng bánh bèo",
   "https://www.instagram.com/nomie.order/p/DCDK9hfT125/", "07/11/2024"),
  ("Top", "Áo len trễ vai", 240000,
   "Áo len trễ vai siêu điệu cho mấy mẻ bánh bèo",
   "https://www.instagram.com/nomie.order/p/DB6D8fgzE_q/", "03/11/2024"),
  ("Top", "Áo CDG 13 De Marzo + gấu", 430000,
   "Size: S - M - L | Màu: Xám - Be | CDG 13 De Marzo kèm gấu (móc khóa/plushie) mã mới siêu ngầu",
   "https://www.instagram.com/nomie.order/p/DAywKOtzqSm/", "07/10/2024"),
]

inserted = 0
for category, name, price, desc, link, posted in products:
    cur.execute("""
        INSERT INTO products (name, price, description, image_url, stock_status, posted_at, category)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, price, desc, link, status(posted), iso(posted), category))
    inserted += 1

conn.commit()
print(f"Inserted {inserted} products")
cur.execute("SELECT COUNT(*), SUM(CASE WHEN stock_status='con_hang' THEN 1 ELSE 0 END) FROM products")
print("Total / con_hang:", cur.fetchone())
conn.close()
