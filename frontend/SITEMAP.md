# 🗺️ Frontend Sitemap & Navigation Flow

## Page Hierarchy

```
┌─────────────────────────────────────────────────────────┐
│                    BOOKSTORE FRONTEND                    │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
    GUEST USER       LOGGED-IN USER        ADMIN USER
  (No auth req)      (Auth required)      (Role = 1)
        │                   │                   │
        ▼                   ▼                   ▼
```

## 📄 Complete Page Structure

### 🌐 Public Pages (No Auth Required)

#### 1. **index.html** (Landing Page)
```
┌─────────────────────────────────┐
│  🏠 HOME PAGE                   │
├─────────────────────────────────┤
│  • Hero section                 │
│  • Featured books (6)           │
│  • Browse by categories         │
│  • Why choose us                │
│  • CTA: Browse Books            │
└─────────────────────────────────┘
        │
        ├──→ books.html (Browse all)
        ├──→ book-detail.html (Click book)
        ├──→ login.html (Login button)
        └──→ register.html (Register button)
```

#### 2. **books.html** (Browse Books)
```
┌─────────────────────────────────┐
│  📚 BROWSE BOOKS                │
├─────────────────────────────────┤
│  Sidebar:                       │
│    • Filter by category         │
│    • Filter by author           │
│    • Min/Max price              │
│    • Apply/Clear buttons        │
│                                 │
│  Main:                          │
│    • Book grid (cards)          │
│    • Add to cart button *       │
│    • View details button        │
└─────────────────────────────────┘
        │
        ├──→ book-detail.html (View details)
        ├──→ cart.html (Add to cart) *
        └──→ login.html (If not logged in) *
        
* Requires authentication
```

#### 3. **book-detail.html** (Book Details)
```
┌─────────────────────────────────┐
│  📖 BOOK DETAILS                │
├─────────────────────────────────┤
│  • Large book image             │
│  • Title, author, price         │
│  • Rating & reviews count       │
│  • Category, stock status       │
│  • Description                  │
│  • Quantity selector            │
│  • Add to cart button *         │
│  • Back to books button         │
│                                 │
│  Reviews Section:               │
│    • Customer reviews (read)    │
│    • Ratings & comments         │
└─────────────────────────────────┘
        │
        ├──→ cart.html (Add to cart) *
        ├──→ books.html (Back)
        └──→ login.html (If not logged in) *
```

#### 4. **login.html** (Login)
```
┌─────────────────────────────────┐
│  🔐 LOGIN                       │
├─────────────────────────────────┤
│  • Username field               │
│  • Password field               │
│  • Login button                 │
│  • Link to register             │
└─────────────────────────────────┘
        │
        ├──→ index.html (Success)
        └──→ register.html (No account)
```

#### 5. **register.html** (Register)
```
┌─────────────────────────────────┐
│  📝 REGISTER                    │
├─────────────────────────────────┤
│  Required:                      │
│    • Username *                 │
│    • Email *                    │
│    • Password *                 │
│                                 │
│  Optional:                      │
│    • Full name                  │
│    • Phone number               │
│    • Address                    │
│    • City                       │
│    • Province                   │
│                                 │
│  • Register button              │
│  • Link to login                │
└─────────────────────────────────┘
        │
        └──→ login.html (Success)
```

---

### 🔒 Protected Pages (Auth Required)

#### 6. **cart.html** (Shopping Cart)
```
┌─────────────────────────────────┐
│  🛒 SHOPPING CART               │
├─────────────────────────────────┤
│  Cart Items:                    │
│    • Book image                 │
│    • Title, author, price       │
│    • Quantity controls (+/-)    │
│    • Remove button              │
│                                 │
│  Order Summary:                 │
│    • Subtotal                   │
│    • Tax (10%)                  │
│    • Total                      │
│    • Checkout button            │
│    • Continue shopping button   │
└─────────────────────────────────┘
        │
        ├──→ checkout.html (Proceed)
        ├──→ books.html (Continue shopping)
        └──→ login.html (If session expired)
```

#### 7. **checkout.html** (Checkout)
```
┌─────────────────────────────────┐
│  💳 CHECKOUT                    │
├─────────────────────────────────┤
│  Shipping Form:                 │
│    • Full name *                │
│    • Phone number *             │
│    • Address *                  │
│    • City *                     │
│    • Province *                 │
│    • Order notes (optional)     │
│                                 │
│  Order Summary:                 │
│    • List of items              │
│    • Subtotal, tax, total       │
│    • Place order button         │
│    • Back to cart button        │
└─────────────────────────────────┘
        │
        ├──→ orders.html (Success)
        └──→ cart.html (Back)
```

#### 8. **orders.html** (Order History)
```
┌─────────────────────────────────┐
│  📦 MY ORDERS                   │
├─────────────────────────────────┤
│  Order Cards:                   │
│    • Order ID                   │
│    • Date                       │
│    • Total amount               │
│    • Status badge               │
│    • View details button        │
│                                 │
│  Order Detail Modal:            │
│    • Complete order info        │
│    • Shipping details           │
│    • Items list                 │
│    • Status                     │
└─────────────────────────────────┘
        │
        └──→ books.html (Empty state)
```

---

## 🧭 Navigation Components

### Top Navbar (All Pages)
```
┌──────────────────────────────────────────────────────────┐
│  📚 Bookstore  [Home] [Books] [Cart 🛒 3]  [User Menu ▼] │
└──────────────────────────────────────────────────────────┘

Guest User Menu:
  • Login
  • Register

Logged-in User Menu:
  • Username ▼
    ├─ My Orders
    ├─ Admin Panel (if admin)
    └─ Logout
```

### Footer (All Pages)
```
┌──────────────────────────────────────────────────────────┐
│  About Us  |  Quick Links  |  Contact                    │
│  © 2025 Bookstore. All rights reserved.                  │
└──────────────────────────────────────────────────────────┘
```

---

## 🔄 User Flows

### Flow 1: Guest Browsing
```
index.html
    ↓
books.html (browse)
    ↓
book-detail.html (view)
    ↓
[Add to Cart] → Redirect to login.html
    ↓
register.html → login.html
    ↓
index.html (logged in)
```

### Flow 2: Complete Purchase
```
login.html (authenticate)
    ↓
books.html (browse)
    ↓
book-detail.html (select)
    ↓
[Add to Cart] ✓
    ↓
cart.html (review)
    ↓
checkout.html (shipping info)
    ↓
[Place Order] ✓
    ↓
orders.html (confirmation)
```

### Flow 3: Returning Customer
```
login.html
    ↓
index.html (home)
    ↓
[Username Menu] → My Orders
    ↓
orders.html (order history)
    ↓
[View Details] → Order detail modal
```

---

## 🎯 Authentication Gates

### Pages Accessible Without Login:
✅ index.html  
✅ books.html  
✅ book-detail.html  
✅ login.html  
✅ register.html  

### Pages Requiring Login:
🔒 cart.html  
🔒 checkout.html  
🔒 orders.html  

### Behavior:
- Accessing protected page without login → Redirect to login.html
- After successful login → Redirect to index.html
- Clicking "Add to Cart" without login → Toast message + Redirect to login.html

---

## 📱 Responsive Breakpoints

### Mobile (< 768px):
- Stacked layout
- Full-width cards
- Collapsed navbar
- Touch-friendly buttons

### Tablet (768px - 991px):
- 2-column book grid
- Sidebar filters below content
- Responsive navbar

### Desktop (≥ 992px):
- 3-column book grid
- Sidebar filters on left
- Full navbar
- Hover effects

---

## 🎨 Visual Elements

### Color-Coded Status Badges:
- 🟡 **Pending** - Yellow
- 🔵 **Processing** - Blue
- 🟣 **Shipped** - Purple
- 🟢 **Delivered** - Green
- 🔴 **Cancelled** - Red

### Interactive Elements:
- ⭐ Star ratings (5-star system)
- 🔔 Toast notifications (success/error/warning/info)
- ⏳ Loading spinners
- 🎴 Book cards with hover effect
- 🔄 Quantity controls (+/-)
- 🗑️ Delete buttons

---

## 📊 State Management

### LocalStorage Keys:
- `access_token` - JWT access token
- `refresh_token` - JWT refresh token
- `user_data` - User information (JSON)
- `cart_items` - Cart data (backup)

### Session Flow:
1. User logs in → Tokens saved
2. Protected API calls → Token attached
3. Token expires → Auto-refresh
4. Refresh fails → Redirect to login
5. User logs out → Clear all storage

---

This sitemap provides a complete overview of your frontend structure! 🗺️✨
