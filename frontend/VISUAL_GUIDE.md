# 🎨 Visual Design Guide

A preview of what your bookstore frontend looks like.

---

## 🌈 Color Palette

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  PRIMARY COLOR:    #8B4513  ████████  Saddle Brown │
│  SECONDARY COLOR:  #D2691E  ████████  Chocolate    │
│  ACCENT COLOR:     #DAA520  ████████  Goldenrod    │
│  BACKGROUND:       #FFF8DC  ████████  Cornsilk     │
│  CARD BG:          #FFFAF0  ████████  Floral White │
│  TEXT DARK:        #3E2723  ████████  Dark Brown   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 📱 Layout Examples

### Landing Page (index.html)

```
┌────────────────────────────────────────────────────────────┐
│  [🕮 Bookstore]  [Home] [Books] [Cart 🛒 0]  [Login] [Reg] │ ← Brown navbar
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│                                                            │
│         📚 Welcome to Your Literary Haven                  │ ← Hero section
│         Discover thousands of books                        │ (gradient brown)
│               [Browse Books]                               │
│                                                            │
└────────────────────────────────────────────────────────────┘

            ✨ Featured Books ✨
         ━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   [IMAGE]   │  │   [IMAGE]   │  │   [IMAGE]   │  ← Book cards
│             │  │             │  │             │  (cream bg)
│ Book Title  │  │ Book Title  │  │ Book Title  │
│ By Author   │  │ By Author   │  │ By Author   │
│ ⭐⭐⭐⭐⭐ (10) │  │ ⭐⭐⭐⭐☆ (8)  │  │ ⭐⭐⭐☆☆ (5)  │
│ $29.99      │  │ $19.99      │  │ $24.99      │
│  [Add 🛒]   │  │  [Add 🛒]   │  │  [Add 🛒]   │
│ [View More] │  │ [View More] │  │ [View More] │
└─────────────┘  └─────────────┘  └─────────────┘

         Browse by Category
         ━━━━━━━━━━━━━━━━

┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│    📖       │  │    📖       │  │    📖       │
│  Fiction    │  │  Non-Fiction│  │  Sci-Fi     │
└─────────────┘  └─────────────┘  └─────────────┘

         Why Choose Us
         ━━━━━━━━━━━━━

┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   🚚        │  │    🛡️       │  │    🎧       │
│   Fast      │  │   Secure    │  │   24/7      │
│  Delivery   │  │  Payment    │  │  Support    │
└─────────────┘  └─────────────┘  └─────────────┘

┌────────────────────────────────────────────────────────────┐
│  © 2025 Bookstore. All rights reserved.                    │ ← Footer
└────────────────────────────────────────────────────────────┘
```

---

### Books Page (books.html)

```
┌────────────────────────────────────────────────────────────┐
│  [🕮 Bookstore]  [Home] [Books*] [Cart 🛒 2]  [@User ▼]    │
└────────────────────────────────────────────────────────────┘

                📚 Browse Books
                ━━━━━━━━━━━━━

┌─────────────┐  ┌─────────────────────────────────────┐
│  FILTERS    │  │  BOOK GRID                          │
│             │  │                                     │
│ Category    │  │  ┌───────┐ ┌───────┐ ┌───────┐     │
│ [Dropdown▼] │  │  │ Book1 │ │ Book2 │ │ Book3 │     │
│             │  │  └───────┘ └───────┘ └───────┘     │
│ Author      │  │                                     │
│ [Dropdown▼] │  │  ┌───────┐ ┌───────┐ ┌───────┐     │
│             │  │  │ Book4 │ │ Book5 │ │ Book6 │     │
│ Min Price   │  │  └───────┘ └───────┘ └───────┘     │
│ [___0.00__] │  │                                     │
│             │  │  ┌───────┐ ┌───────┐ ┌───────┐     │
│ Max Price   │  │  │ Book7 │ │ Book8 │ │ Book9 │     │
│ [__100.00_] │  │  └───────┘ └───────┘ └───────┘     │
│             │  │                                     │
│ [Apply]     │  │                                     │
│ [Clear]     │  │                                     │
└─────────────┘  └─────────────────────────────────────┘
```

---

### Book Detail Page (book-detail.html)

```
┌────────────────────────────────────────────────────────────┐
│  [🕮 Bookstore]  [Home] [Books] [Cart 🛒 2]  [@User ▼]     │
└────────────────────────────────────────────────────────────┘

┌─────────────────┐  ┌─────────────────────────────────────┐
│                 │  │  The Great Gatsby                   │
│                 │  │  by F. Scott Fitzgerald             │
│    [BOOK        │  │                                     │
│     IMAGE]      │  │  ⭐⭐⭐⭐⭐ 4.5/5.0 (127 reviews)      │
│                 │  │                                     │
│                 │  │  [Fiction] [In Stock (15)]          │
│                 │  │                                     │
│                 │  │  💰 $24.99                          │
└─────────────────┘  │                                     │
                     │  Description:                       │
                     │  A classic novel set in the Jazz    │
                     │  Age that tells the story of...     │
                     │                                     │
                     │  Quantity: [-] [1] [+]              │
                     │                                     │
                     │  [🛒 Add to Cart]                   │
                     │  [← Back to Books]                  │
                     └─────────────────────────────────────┘

         Customer Reviews
         ━━━━━━━━━━━━━━━━

┌────────────────────────────────────────────────────────────┐
│  John Doe                           Dec 20, 2025           │
│  ⭐⭐⭐⭐⭐                                                    │
│  "Amazing book! Highly recommended..."                     │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│  Jane Smith                         Dec 18, 2025           │
│  ⭐⭐⭐⭐☆                                                    │
│  "Great read, but ending was..."                           │
└────────────────────────────────────────────────────────────┘
```

---

### Shopping Cart (cart.html)

```
┌────────────────────────────────────────────────────────────┐
│  [🕮 Bookstore]  [Home] [Books] [Cart 🛒 3*]  [@User ▼]    │
└────────────────────────────────────────────────────────────┘

                🛒 Shopping Cart
                ━━━━━━━━━━━━━━━

┌──────────────────────────────────┐  ┌──────────────────┐
│  CART ITEMS                      │  │  ORDER SUMMARY   │
│                                  │  │                  │
│  ┌────────────────────────────┐  │  │  Subtotal:       │
│  │ [IMG] Book Title 1         │  │  │  $74.97          │
│  │       By Author            │  │  │                  │
│  │       $24.99               │  │  │  Tax (10%):      │
│  │       [-][2][+]   [🗑️]     │  │  │  $7.50           │
│  │       Subtotal: $49.98     │  │  │                  │
│  └────────────────────────────┘  │  │  Total:          │
│                                  │  │  $82.47          │
│  ┌────────────────────────────┐  │  │  ━━━━━━━━━━━━━━  │
│  │ [IMG] Book Title 2         │  │  │                  │
│  │       By Author            │  │  │  [💳 Checkout]   │
│  │       $24.99               │  │  │                  │
│  │       [-][1][+]   [🗑️]     │  │  │  [← Continue     │
│  │       Subtotal: $24.99     │  │  │     Shopping]    │
│  └────────────────────────────┘  │  └──────────────────┘
│                                  │
└──────────────────────────────────┘
```

---

### Checkout Page (checkout.html)

```
┌────────────────────────────────────────────────────────────┐
│  [🕮 Bookstore]  [Home] [Books] [Cart 🛒 3]  [@User ▼]     │
└────────────────────────────────────────────────────────────┘

                💳 Checkout
                ━━━━━━━━━━━

┌──────────────────────────────────┐  ┌──────────────────┐
│  SHIPPING INFORMATION            │  │  ORDER SUMMARY   │
│                                  │  │                  │
│  Full Name:                      │  │  • Book 1 (x2)   │
│  [____________________]          │  │    $49.98        │
│                                  │  │  • Book 2 (x1)   │
│  Phone Number:                   │  │    $24.99        │
│  [____________________]          │  │                  │
│                                  │  │  ━━━━━━━━━━━━━━  │
│  Address:                        │  │  Subtotal:       │
│  [____________________]          │  │  $74.97          │
│                                  │  │                  │
│  City:          Province:        │  │  Tax (10%):      │
│  [__________]   [__________]     │  │  $7.50           │
│                                  │  │                  │
│  Order Notes (Optional):         │  │  Total:          │
│  [____________________]          │  │  $82.47          │
│  [____________________]          │  │  ━━━━━━━━━━━━━━  │
│  [____________________]          │  │                  │
│                                  │  │  [✓ Place Order] │
│                                  │  │                  │
│                                  │  │  [← Back to Cart]│
└──────────────────────────────────┘  └──────────────────┘
```

---

### Orders Page (orders.html)

```
┌────────────────────────────────────────────────────────────┐
│  [🕮 Bookstore]  [Home] [Books] [Cart 🛒 0]  [@User ▼]     │
└────────────────────────────────────────────────────────────┘

                📦 My Orders
                ━━━━━━━━━━━━

┌────────────────────────────────────────────────────────────┐
│  Order #abc123     Dec 25, 2025    $82.47    [Delivered]  │
│                                             [View Details] │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│  Order #def456     Dec 20, 2025    $45.99    [Shipped]    │
│                                             [View Details] │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│  Order #ghi789     Dec 15, 2025    $125.50   [Processing] │
│                                             [View Details] │
└────────────────────────────────────────────────────────────┘

         [Order Detail Modal]
         
┌────────────────────────────────────────────┐
│  Order Details                       [✕]   │
├────────────────────────────────────────────┤
│  Order ID: #abc123                         │
│  Status: [Delivered]                       │
│  Date: Dec 25, 2025                        │
│  Total: $82.47                             │
│                                            │
│  Shipping Information:                     │
│  John Doe                                  │
│  (555) 123-4567                            │
│  123 Main St                               │
│  New York, NY                              │
│                                            │
│  Items:                                    │
│  • The Great Gatsby (x2) - $49.98          │
│  • 1984 (x1) - $24.99                      │
│                                            │
│  Subtotal: $74.97                          │
│  Tax: $7.50                                │
│  Total: $82.47                             │
└────────────────────────────────────────────┘
```

---

### Login Page (login.html)

```
┌────────────────────────────────────────────────────────────┐
│  [🕮 Bookstore]  [Home] [Books] [Cart 🛒 0]  [Login] [Reg] │
└────────────────────────────────────────────────────────────┘


                ┌──────────────────┐
                │   🔐 Login       │
                ├──────────────────┤
                │                  │
                │  Username:       │
                │  [____________]  │
                │                  │
                │  Password:       │
                │  [____________]  │
                │                  │
                │  [🔐 Login]      │
                │                  │
                │  Don't have an   │
                │  account?        │
                │  Register here   │
                │                  │
                └──────────────────┘
```

---

### Register Page (register.html)

```
┌────────────────────────────────────────────────────────────┐
│  [🕮 Bookstore]  [Home] [Books] [Cart 🛒 0]  [Login] [Reg] │
└────────────────────────────────────────────────────────────┘


            ┌──────────────────────────────┐
            │   📝 Register                │
            ├──────────────────────────────┤
            │                              │
            │  Username* [___] Email* [___]│
            │                              │
            │  Password* [___] Name   [___]│
            │                              │
            │  Phone     [___] City   [___]│
            │                              │
            │  Address:                    │
            │  [_________________________] │
            │                              │
            │  Province/State:             │
            │  [_________________________] │
            │                              │
            │  [📝 Register]               │
            │                              │
            │  Already have an account?    │
            │  Login here                  │
            │                              │
            └──────────────────────────────┘
```

---

## 🎨 UI Components

### Toast Notifications

```
┌─────────────────────────────────┐
│ ✓ Success                 [✕]   │  ← Green background
│ Book added to cart!             │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ ⚠ Warning                 [✕]   │  ← Yellow background
│ Please login to continue        │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ ✕ Error                   [✕]   │  ← Red background
│ Failed to load books            │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ ℹ Info                    [✕]   │  ← Blue background
│ Loading your cart...            │
└─────────────────────────────────┘
```

### Status Badges

```
[Pending]      ← Yellow badge
[Processing]   ← Blue badge
[Shipped]      ← Purple badge
[Delivered]    ← Green badge
[Cancelled]    ← Red badge
```

### Star Ratings

```
⭐⭐⭐⭐⭐  5.0 (Full stars)
⭐⭐⭐⭐☆  4.0 (4 full + 1 empty)
⭐⭐⭐½☆  3.5 (3 full + 1 half + 1 empty)
⭐⭐☆☆☆  2.0 (2 full + 3 empty)
⭐☆☆☆☆  1.0 (1 full + 4 empty)
```

### Loading Spinner

```
    ⏳
  Loading...
```

### Quantity Controls

```
┌───┬─────┬───┐
│ - │  3  │ + │
└───┴─────┴───┘
```

---

## 📱 Responsive Layouts

### Desktop (> 992px)
```
┌────────────────────────────────────────┐
│  Navbar (full)                         │
└────────────────────────────────────────┘
┌────┬────────────────────────────┬──────┐
│Fil-│  [Book] [Book] [Book]      │ Side │
│ters│  [Book] [Book] [Book]      │ bar  │
│    │  [Book] [Book] [Book]      │      │
└────┴────────────────────────────┴──────┘
```

### Tablet (768px - 991px)
```
┌────────────────────────────────────────┐
│  Navbar (condensed)                    │
└────────────────────────────────────────┘
┌────────────────────────────────────────┐
│  [Book] [Book]                         │
│  [Book] [Book]                         │
│  [Book] [Book]                         │
└────────────────────────────────────────┘
┌────────────────────────────────────────┐
│  Filters (below)                       │
└────────────────────────────────────────┘
```

### Mobile (< 768px)
```
┌──────────────────┐
│ Navbar (burger)  │
└──────────────────┘
┌──────────────────┐
│                  │
│    [Book]        │
│                  │
│    [Book]        │
│                  │
│    [Book]        │
│                  │
└──────────────────┘
```

---

## 🎯 Visual Hierarchy

### Typography Sizes

```
H1:  3rem (48px) - Page titles
H2:  2.5rem (40px) - Section titles  
H3:  2rem (32px) - Card titles
H4:  1.5rem (24px) - Subsection titles
H5:  1.25rem (20px) - Small headings
Body: 1rem (16px) - Regular text
Small: 0.875rem (14px) - Meta info
```

### Spacing

```
Section Gap:     4rem (64px)
Card Padding:    1.5rem (24px)
Element Margin:  1rem (16px)
Button Padding:  0.75rem 1.5rem
```

---

## 🖼️ Book Card Anatomy

```
┌─────────────────────────┐
│                         │
│     [BOOK IMAGE]        │  ← 300px height
│                         │
│                         │
├─────────────────────────┤
│  Book Title Here That   │  ← 2 lines max
│  May Span Two Lines     │
│                         │
│  by Author Name         │  ← Muted text
│                         │
│  ⭐⭐⭐⭐⭐ (125)          │  ← Gold stars
│                         │
│  $29.99    [Add 🛒]     │  ← Gold price, brown btn
│                         │
│  [View Details]         │  ← Gold button
│                         │
└─────────────────────────┘
     ↓ Hover Effect ↓
┌─────────────────────────┐  ← Lifts up
│       (shadow)          │  ← Larger shadow
└─────────────────────────┘
```

---

This visual guide shows you exactly what your bookstore looks like! 🎨✨
