# ✅ Frontend Testing Checklist

Use this checklist to verify all features are working correctly.

---

## 🚀 Pre-Testing Setup

- [ ] Flask API is running at `http://localhost:5000`
- [ ] Frontend is served (Live Server or HTTP server)
- [ ] Browser DevTools open (F12) to check console
- [ ] At least 3-5 books seeded in database
- [ ] At least 2 categories and 2 authors exist

---

## 📝 Test 1: Guest User Flow

### Landing Page (index.html)
- [ ] Page loads without errors
- [ ] Navbar shows "Login" and "Register" buttons
- [ ] Hero section displays correctly
- [ ] Featured books section shows 6 books
- [ ] Book cards have:
  - [ ] Image (or placeholder SVG)
  - [ ] Title
  - [ ] Author name
  - [ ] Star rating
  - [ ] Price
  - [ ] "Add" button
  - [ ] "View Details" button
- [ ] "Browse by Category" section displays categories
- [ ] Footer is visible
- [ ] No console errors

### Browse Books (books.html)
- [ ] Navigate to books page via navbar or CTA button
- [ ] All books display in grid layout
- [ ] Filters sidebar shows:
  - [ ] Category dropdown (populated)
  - [ ] Author dropdown (populated)
  - [ ] Min price input
  - [ ] Max price input
  - [ ] Apply Filters button
  - [ ] Clear button
- [ ] Apply category filter → Books filter correctly
- [ ] Apply author filter → Books filter correctly
- [ ] Apply price range → Books filter correctly
- [ ] Clear filters → All books return
- [ ] Book cards display properly
- [ ] Click "Add to Cart" (guest) → Shows warning toast → Redirects to login

### Book Detail (book-detail.html)
- [ ] Click "View Details" on any book
- [ ] Page loads with URL parameter (?id=...)
- [ ] Large book image displays
- [ ] All book info shows:
  - [ ] Title
  - [ ] Author
  - [ ] Category badge
  - [ ] Stock status badge
  - [ ] Price (gold color)
  - [ ] Rating stars
  - [ ] Description
- [ ] Quantity controls work:
  - [ ] Increment button works
  - [ ] Decrement button works (stops at 1)
  - [ ] Cannot exceed stock quantity
- [ ] "Add to Cart" (guest) → Warning → Redirect to login
- [ ] "Back to Books" button works
- [ ] Reviews section shows (if available)

---

## 🔐 Test 2: Authentication Flow

### Register (register.html)
- [ ] Navigate to register page
- [ ] Form displays all fields:
  - [ ] Username (required)
  - [ ] Email (required)
  - [ ] Password (required)
  - [ ] Name (optional)
  - [ ] Phone (optional)
  - [ ] Address (optional)
  - [ ] City (optional)
  - [ ] Province (optional)
- [ ] Test validations:
  - [ ] Empty username → Error
  - [ ] Invalid email format → Error
  - [ ] Short password (< 6 chars) → Error
  - [ ] Invalid username format → Error
- [ ] Submit valid form:
  - [ ] Success toast appears
  - [ ] Redirects to login page after 1.5s
- [ ] "Login here" link works

### Login (login.html)
- [ ] Navigate to login page
- [ ] Form displays:
  - [ ] Username field
  - [ ] Password field
  - [ ] Login button
- [ ] Test with wrong credentials → Error toast
- [ ] Test with correct credentials:
  - [ ] Success toast appears
  - [ ] Redirects to home page
  - [ ] Navbar shows username dropdown
  - [ ] "Login/Register" replaced with username
- [ ] "Register here" link works

### Auth State
- [ ] Username appears in navbar
- [ ] Dropdown menu shows:
  - [ ] "My Orders"
  - [ ] "Logout"
  - [ ] "Admin Panel" (if admin user)
- [ ] Cart badge shows "0"
- [ ] Refresh page → Still logged in
- [ ] Open new tab → Still logged in (shared localStorage)

---

## 🛒 Test 3: Shopping Flow (Logged In)

### Add to Cart
- [ ] Go to books page
- [ ] Click "Add to Cart" on a book → Success toast
- [ ] Cart badge updates to "1"
- [ ] Add same book again → Badge updates to "2"
- [ ] Add different book → Badge increases
- [ ] No console errors

### Cart Page (cart.html)
- [ ] Click cart icon in navbar
- [ ] Cart page loads
- [ ] Items display with:
  - [ ] Book image
  - [ ] Title
  - [ ] Author
  - [ ] Price per unit
  - [ ] Quantity controls
  - [ ] Subtotal per item
  - [ ] Remove button
- [ ] Test quantity controls:
  - [ ] Click "+" → Quantity increases → Subtotal updates
  - [ ] Click "-" → Quantity decreases → Subtotal updates
  - [ ] Decrease to 0 → Prompts removal
- [ ] Test remove button:
  - [ ] Click trash icon → Confirmation prompt
  - [ ] Confirm → Item removed → Cart updates
- [ ] Order summary shows:
  - [ ] Subtotal (sum of all items)
  - [ ] Tax (10% of subtotal)
  - [ ] Total (subtotal + tax)
- [ ] "Proceed to Checkout" button enabled
- [ ] "Continue Shopping" button works

### Empty Cart
- [ ] Remove all items
- [ ] Empty state displays:
  - [ ] Cart icon
  - [ ] "Your cart is empty" message
  - [ ] "Browse Books" button
- [ ] "Proceed to Checkout" disabled

---

## 💳 Test 4: Checkout Flow

### Checkout Page (checkout.html)
- [ ] Add items to cart first
- [ ] Click "Proceed to Checkout"
- [ ] Checkout page loads
- [ ] Shipping form displays
- [ ] User data pre-filled (if available in profile)
- [ ] Order items summary shows:
  - [ ] List of books with quantities
  - [ ] Individual prices
- [ ] Order summary shows:
  - [ ] Subtotal
  - [ ] Tax
  - [ ] Total
- [ ] Test form validations:
  - [ ] Empty required fields → Error
  - [ ] All fields filled → Submit enabled
- [ ] Fill valid data and submit:
  - [ ] Button shows "Processing..." spinner
  - [ ] Success toast appears
  - [ ] Redirects to orders page after 1.5s
- [ ] "Back to Cart" button works

---

## 📦 Test 5: Orders

### Orders Page (orders.html)
- [ ] Navigate via username dropdown → "My Orders"
- [ ] Orders page loads
- [ ] Order cards display:
  - [ ] Order ID (shortened)
  - [ ] Order date
  - [ ] Total amount
  - [ ] Status badge (colored)
  - [ ] "View Details" button
- [ ] Orders sorted by date (newest first)
- [ ] Click "View Details":
  - [ ] Modal opens
  - [ ] Complete order information shows:
    - [ ] Order ID
    - [ ] Status
    - [ ] Date
    - [ ] Shipping info (name, phone, address, city, province)
    - [ ] Order notes (if any)
    - [ ] Items table with prices
    - [ ] Subtotal, tax, total breakdown
- [ ] Modal closes properly

### Empty Orders
- [ ] New user with no orders
- [ ] Empty state displays:
  - [ ] Box icon
  - [ ] "No orders yet" message
  - [ ] "Browse Books" button

---

## 🎨 Test 6: UI/UX Elements

### Toast Notifications
- [ ] Success toast (green) appears for:
  - [ ] Login success
  - [ ] Registration success
  - [ ] Add to cart
  - [ ] Cart update
  - [ ] Order placed
- [ ] Error toast (red) appears for:
  - [ ] Login failed
  - [ ] API errors
  - [ ] Network errors
- [ ] Warning toast (yellow) appears for:
  - [ ] Login required actions
- [ ] Toast auto-dismisses after 5 seconds
- [ ] Toast has close button

### Loading States
- [ ] Loading spinner shows when:
  - [ ] Fetching books
  - [ ] Loading book details
  - [ ] Loading cart
  - [ ] Loading orders
  - [ ] Submitting forms
- [ ] Content replaces spinner after load

### Responsive Design
- [ ] Desktop view (> 992px):
  - [ ] 3-column book grid
  - [ ] Sidebar filters on left
  - [ ] Full navbar
- [ ] Tablet view (768px - 991px):
  - [ ] 2-column book grid
  - [ ] Filters below or collapsed
- [ ] Mobile view (< 768px):
  - [ ] 1-column book grid
  - [ ] Stacked layout
  - [ ] Hamburger menu
  - [ ] Touch-friendly buttons

---

## 🔄 Test 7: Advanced Features

### Token Refresh
- [ ] Login and wait (token expires after set time)
- [ ] Make protected API call
- [ ] Token auto-refreshes (check network tab)
- [ ] Request succeeds without re-login
- [ ] If refresh fails → Redirect to login

### Cart Persistence
- [ ] Add items to cart
- [ ] Refresh page → Cart persists
- [ ] Close browser and reopen → Cart persists (if logged in)
- [ ] Logout → Cart clears

### Back Navigation
- [ ] Use browser back button on each page
- [ ] Pages navigate correctly
- [ ] State is preserved
- [ ] No errors in console

### URL Direct Access
- [ ] Copy book detail URL → Paste in new tab → Works
- [ ] Try accessing cart.html without login → Redirects to login
- [ ] Try accessing orders.html without login → Redirects to login

---

## 🐛 Test 8: Error Handling

### Network Errors
- [ ] Stop Flask API
- [ ] Try loading books → Error message shows
- [ ] Try login → Error toast appears
- [ ] Try add to cart → Error toast
- [ ] Start API → Everything works again

### Invalid Data
- [ ] Try accessing book with fake ID (?id=invalid)
  - [ ] Error message shows
  - [ ] "Back to books" link works
- [ ] Try accessing order with fake ID
  - [ ] Error handled gracefully

### Edge Cases
- [ ] Book with no image → Placeholder shows
- [ ] Book with no reviews → "No reviews" message
- [ ] Empty book list → Empty state shows
- [ ] Very long book title → Text truncates with ellipsis
- [ ] Book with 0 stock → "Out of Stock" badge + Add button disabled

---

## 🎯 Test 9: Cross-Browser Testing

Test on multiple browsers:

### Chrome
- [ ] All features work
- [ ] UI renders correctly
- [ ] No console errors

### Firefox
- [ ] All features work
- [ ] UI renders correctly
- [ ] No console errors

### Safari (if available)
- [ ] All features work
- [ ] UI renders correctly
- [ ] No console errors

### Edge
- [ ] All features work
- [ ] UI renders correctly
- [ ] No console errors

---

## 🔒 Test 10: Security

### Authentication
- [ ] Cannot access cart without login
- [ ] Cannot access checkout without login
- [ ] Cannot access orders without login
- [ ] Token stored in localStorage (check Application tab)
- [ ] Logout clears all tokens

### CSRF Protection
- [ ] API uses JWT (no CSRF needed)
- [ ] No sensitive data in URL

---

## ✅ Final Checklist

- [ ] All pages load without errors
- [ ] All forms validate correctly
- [ ] All buttons work as expected
- [ ] All links navigate correctly
- [ ] Responsive design works on all screen sizes
- [ ] Toast notifications appear for user actions
- [ ] Loading states show during async operations
- [ ] Error handling works for all failure cases
- [ ] Authentication flow is secure
- [ ] Cart and order flows complete successfully
- [ ] No console errors or warnings
- [ ] Images load or show placeholders
- [ ] Typography is readable and consistent
- [ ] Colors match the bookstore theme
- [ ] Footer displays on all pages

---

## 📊 Performance Checklist

- [ ] Pages load in < 2 seconds (with API)
- [ ] Images are optimized or lazy-loaded
- [ ] No memory leaks (check DevTools Performance tab)
- [ ] Smooth animations and transitions
- [ ] No layout shifts during load

---

## 🎉 Testing Complete!

If all items are checked ✅, your bookstore frontend is **production-ready**!

### Found Issues?
1. Check browser console for errors
2. Verify Flask API is running and returning correct data
3. Check `config.js` for correct API URL
4. Clear localStorage and try again: `localStorage.clear()`

### Next Steps:
- Deploy to production
- Add analytics (Google Analytics, etc.)
- Implement additional features (admin panel, reviews, etc.)
- Optimize performance
- Add SEO meta tags

**Happy testing! 🧪✨**
