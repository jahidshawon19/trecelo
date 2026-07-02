# Trecelo — Sample Tracking System
## User Documentation

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Accessing the Application](#2-accessing-the-application)
3. [User Roles Overview](#3-user-roles-overview)
4. [Logging In & Out](#4-logging-in--out)
5. [Dashboard](#5-dashboard)
6. [Samples](#6-samples)
   - 6.1 [Viewing the Sample List](#61-viewing-the-sample-list)
   - 6.2 [Searching & Filtering Samples](#62-searching--filtering-samples)
   - 6.3 [Viewing a Sample Detail](#63-viewing-a-sample-detail)
   - 6.4 [Creating a Sample](#64-creating-a-sample)
   - 6.5 [Editing a Sample](#65-editing-a-sample)
   - 6.6 [Deleting a Sample](#66-deleting-a-sample)
   - 6.7 [Exporting Samples](#67-exporting-samples)
7. [Makers (Staff)](#7-makers-staff)
   - 7.1 [Viewing the Maker List](#71-viewing-the-maker-list)
   - 7.2 [Viewing a Maker's Profile](#72-viewing-a-makers-profile)
   - 7.3 [Adding a Maker](#73-adding-a-maker)
   - 7.4 [Editing a Maker](#74-editing-a-maker)
   - 7.5 [Deleting a Maker](#75-deleting-a-maker)
   - 7.6 [Updating Your Own Profile (Makers)](#76-updating-your-own-profile-makers)
8. [Buyers](#8-buyers)
   - 8.1 [Viewing the Buyer List](#81-viewing-the-buyer-list)
   - 8.2 [Viewing a Buyer's Profile](#82-viewing-a-buyers-profile)
   - 8.3 [Adding a Buyer](#83-adding-a-buyer)
   - 8.4 [Editing a Buyer](#84-editing-a-buyer)
   - 8.5 [Deleting a Buyer](#85-deleting-a-buyer)
9. [Brands](#9-brands)
10. [Categories](#10-categories)
11. [GGs](#11-ggs)
12. [Challenges In](#12-challenges-in)
13. [Top Management Accounts](#13-top-management-accounts)
14. [General Customer Accounts](#14-general-customer-accounts)
15. [Role-by-Role Quick Reference](#15-role-by-role-quick-reference)
16. [Frequently Asked Questions](#16-frequently-asked-questions)

---

## 1. Introduction

**Trecelo** is a web-based Sample Tracking System designed to manage the lifecycle of product samples — from creation and submission through to approval or rejection. It connects makers, buyers, and management in a single platform with clearly defined roles and real-time visibility.

### Key capabilities
- Track samples with detailed technical specifications, images, and documents
- Manage makers (staff), buyers, brands, categories, and lookup data
- Role-based access so every user sees exactly what they need
- Dashboard charts and analytics for at-a-glance oversight
- Export sample reports to PDF or Excel

---

## 2. Accessing the Application

Open your web browser and go to the application URL provided to you by your administrator (e.g. `https://your-domain.com`). The login page will appear immediately.

> **Tip:** Bookmark the URL for quick access. If you are unsure of the address, contact your Super Admin.

---

## 3. User Roles Overview

Trecelo has **five user roles**. Your role is assigned by the Super Admin and determines which pages you can see and what actions you can take.

| Role | Badge Colour | Who they are | Key capability |
|---|---|---|---|
| **Super Admin** | 🔴 Red | System owner / IT admin | Full control — create, edit, delete everything |
| **Maker** | 🔵 Blue | Factory / production staff | Create and manage samples |
| **Buyer** | 🟢 Green | Customer / purchasing org | View samples for their brands only |
| **Top Management** | 🟣 Purple | Leadership / executives | View-only access to all data |
| **General Customer** | 🩵 Teal | External viewer | View-only access to all data |

Your current role is displayed as a badge in the top-right corner of every page, and your role label appears beneath your username in both the sidebar and the top bar.

---

## 4. Logging In & Out

### Logging In

1. Go to the application URL — you will land on the **Login** page.
2. Enter your **Username** and **Password** exactly as provided by your administrator (passwords are case-sensitive).
3. Click **Login**.
4. You will be redirected to the **Dashboard**.

If you see the message *"Invalid username or password"*, double-check your credentials. If you have forgotten your password, contact your Super Admin — they can reset it for you.

### Logging Out

Click the red **Logout** button in the top-right corner of the page. You will be returned to the Login page immediately.

> **Important:** Always log out when using a shared or public computer.

---

## 5. Dashboard

The Dashboard is the first page you see after logging in. It gives you a visual summary of all sample activity.

**To reach it at any time:** Click **Dashboard** in the left sidebar.

### What you will see

| Section | Description |
|---|---|
| **Total Samples** | Count of all samples visible to your role |
| **Approved** | Samples with Approved status |
| **Pending** | Samples awaiting a decision |
| **Draft** | Samples still being prepared |
| **Rejected** | Samples that did not pass |
| **Total Buyers** | Number of buyer accounts (Super Admin / Management only) |
| **Total Makers** | Number of maker accounts (Super Admin / Management only) |

### Charts

- **Status Doughnut Chart** — Visual breakdown of sample statuses
- **Top Buyers Bar Chart** — Which buyers have the most samples (top 8)
- **Monthly Submissions Line Chart** — Sample submission trend over time
- **Sample Type Pie Chart** — Distribution across the top 6 sample types

### Brand Logos

If brand logos have been uploaded, they are displayed in a row at the bottom of the Dashboard for quick reference.

> **Note for Buyers:** Your dashboard only shows samples linked to the brands assigned to your account. Your assigned brand logos also appear in the top navigation bar.

---

## 6. Samples

Samples are the core of Trecelo. A sample record captures everything about a physical product sample — its specifications, images, status, and associated parties.

### 6.1 Viewing the Sample List

Click **Samples** in the left sidebar. You will see a paginated table showing:

| Column | Description |
|---|---|
| **#** | Row counter |
| **Style Number** | Sample's unique style code |
| **Buyer** | Associated buyer name |
| **Sample Type** | Type/category of sample |
| **GG** | Associated GG value(s) |
| **Color** | Sample colour |
| **Season** | Season number |
| **Submission Date** | Date submitted |
| **Status** | Current status badge (Approved / Pending / Draft / Rejected) |
| **Actions** | View, Edit, Delete buttons (Edit/Delete visible to Makers and Super Admin only) |

The list shows **10 samples per page**. Use the pagination controls at the bottom to move between pages.

### 6.2 Searching & Filtering Samples

At the top of the Sample list there are two controls:

**Search box** — Type any keyword to search across:
- Style Number
- Buyer Name
- Sample Type
- Color
- Season

**Status filter** — Use the dropdown to show only samples of a specific status:
- All (default)
- Pending
- Approved
- Draft
- Rejected

Both controls can be used together. The list updates after you press **Enter** or click **Filter**.

### 6.3 Viewing a Sample Detail

Click the **eye icon** (👁) on any sample row, or click the style number link. The detail page shows:

**Basic Information**
- Style Number, Sample Type, Color, Season
- Status badge
- Submission Date
- Associated Buyer, Maker(s), Brand(s), Category(ies)

**Technical Specifications**
- GG, Size, Weight
- Yarn Composition, Yarn Consumption
- Moisture Level
- Description
- Challenges In

**Images**
- Front Part Image
- Back Part Image
- Tech Pack
- Challenge Images (gallery)

**Documents**
- Downloadable attached document (if uploaded)

> **Note for Buyers:** You can only view detail pages for samples belonging to your assigned brands. Trying to access another sample will show an access-denied message.

### 6.4 Creating a Sample

> **Who can do this:** Makers and Super Admin only.

1. Click **Samples** in the sidebar, then click the **Add Sample** button (top right).
2. Fill in the form fields. Fields marked with an asterisk (*) are required — however most fields are optional to allow saving drafts.

**Form sections:**

*Basic Information*
- **Style Number** — Unique code for this sample (e.g. `TR-2024-001`)
- **Sample Type** — e.g. Proto, Fit, Salesman, TOP
- **Color** — Colour name or code
- **Season** — Numeric season identifier
- **Status** — Choose: Draft, Pending, Approved, or Rejected
- **Submission Date** — Use the date picker

*Relations*
- **Category** — Select one or more categories (hold Ctrl/Cmd to multi-select)
- **Brand** — Select one or more brands
- **Buyer** — Select the associated buyer (the Buyer dropdown auto-filters based on the selected Brand)
- **Maker** — Select the maker(s) responsible

*Technical Specifications*
- **GG** — Select applicable GGs
- **Size, Weight** — Free text
- **Yarn Composition, Yarn Consumption** — Free text
- **Moisture Level** — Free text
- **Description** — Additional notes
- **Challenge In** — Select any identified challenges (checkboxes)

*Images & Documents*
- **Front Part Image** — Upload a front view photo
- **Back Part Image** — Upload a back view photo
- **Tech Pack** — Upload a tech pack image
- **Documents** — Upload a supporting document (PDF, Word, etc.)
- **Challenge Images** — Upload one or more challenge/issue photos

> **Image tip:** Images are automatically compressed on upload — you do not need to resize them manually.

3. Click **Save** to create the sample.

### 6.5 Editing a Sample

> **Who can do this:** Makers and Super Admin only.

1. Find the sample in the list and click the **pencil icon** (✏️).
2. Modify any fields as needed.
3. To **remove** an existing Challenge Image, tick the checkbox next to it before saving.
4. To **add** new Challenge Images, use the upload field at the bottom of the images section.
5. Click **Save** to apply your changes.

### 6.6 Deleting a Sample

> **Who can do this:** Makers and Super Admin only.

1. Find the sample in the list and click the **trash icon** (🗑).
2. A confirmation page will appear showing the sample name.
3. Click **Confirm Delete** to permanently remove it, or click **Cancel** / your browser's back button to go back.

> **Warning:** Deletion is permanent and cannot be undone.

### 6.7 Exporting Samples

You can export the currently filtered/searched page of samples in two formats.

**Export as PDF**
1. Apply any search or filter to show the samples you want.
2. Click the **Export PDF** button.
3. A PDF file will download containing a formatted table with columns: #, Style No, Buyer, Sample Type, GG, Color, Season, Submission Date, Status.

**Export as Excel**
1. Apply any search or filter to show the samples you want.
2. Click the **Export Excel** button.
3. An `.xlsx` file will download with the same columns, styled with header formatting.

> **Note:** Only the samples on the **current page** (up to 10) are exported. To export more, increase the page size or export each page separately.

---

## 7. Makers (Staff)

Makers are the production staff who create and manage samples.

### 7.1 Viewing the Maker List

> **Who can do this:** Super Admin, Top Management, General Customer.

Click **Maker** under the Management section in the sidebar. The list shows each maker's profile picture/avatar, name, employee ID, role, designation, and phone number.

Use the **search box** at the top to filter by name, username, employee ID, role, or designation.

### 7.2 Viewing a Maker's Profile

Click the **eye icon** (👁) on any maker row. The detail page shows:
- Full profile information (employee ID, role, designation, address, NID, phone)
- A table of all samples assigned to that maker

### 7.3 Adding a Maker

> **Who can do this:** Super Admin only.

1. Go to **Maker** in the sidebar and click **Add Member**.
2. Fill in all required fields:

| Field | Description |
|---|---|
| **Username** | Login username for the new maker |
| **Password** | Initial login password |
| **Maker Name** | Display name (optional) |
| **Employee ID** | Unique employee identifier |
| **Role** | Job role (e.g. Pattern Maker, QC Inspector) |
| **Designation** | Job title |
| **Address** | Physical address |
| **NID** | National ID number |
| **Phone Number** | Contact number (max 11 digits) |
| **Profile Picture** | Upload a photo (optional) |

3. Click **Save**. The new maker can now log in with the username and password you set.

> **Note:** Maker accounts are automatically granted staff-level access (they can create and edit samples).

### 7.4 Editing a Maker

> **Who can do this:** Super Admin only.

1. In the Maker list, click the **pencil icon** (✏️) for the maker you want to edit.
2. Update any fields.
3. To change the password, enter a new one in the **Password** field. Leave it blank to keep the existing password.
4. Click **Save**.

### 7.5 Deleting a Maker

> **Who can do this:** Super Admin only.

1. In the Maker list, click the **trash icon** (🗑).
2. Confirm the deletion on the next page.

> **Warning:** Deleting a maker also deletes their associated login account. This cannot be undone.

### 7.6 Updating Your Own Profile (Makers)

Makers can update their own profile picture without contacting the Super Admin.

1. Click **My Profile** in the **Account** section of the sidebar.
2. Click on the profile picture upload field and select a new image.
3. Click **Save**.

---

## 8. Buyers

Buyers are the purchasing organisations or individuals associated with specific brands. Each buyer has a dedicated login that shows them only the samples relevant to their brands.

### 8.1 Viewing the Buyer List

> **Who can do this:** Super Admin, Top Management, General Customer.

Click **Buyers** under the Management section in the sidebar. The list shows each buyer's name, username, and their associated brands.

Use the **search box** to filter by name, username, or brand.

### 8.2 Viewing a Buyer's Profile

Click the **eye icon** (👁) on any buyer row. The detail page shows:
- Buyer name and username
- All brands assigned to this buyer
- A table of all samples linked to this buyer

### 8.3 Adding a Buyer

> **Who can do this:** Super Admin only.

1. Go to **Buyers** in the sidebar and click **Add Buyer**.
2. Fill in the form:

| Field | Description |
|---|---|
| **Username** | Login username for the buyer |
| **Password** | Initial login password |
| **Buyer Name** | Organisation or person's display name |
| **Brands** | Select one or more brands this buyer can see (hold Ctrl/Cmd to multi-select) |

3. Click **Save**.

### 8.4 Editing a Buyer

> **Who can do this:** Super Admin only.

1. In the Buyer list, click the **pencil icon** (✏️).
2. Update any fields. Leave **Password** blank to keep the current password.
3. To add or remove brand assignments, update the **Brands** multi-select.
4. Click **Save**.

### 8.5 Deleting a Buyer

> **Who can do this:** Super Admin only.

1. In the Buyer list, click the **trash icon** (🗑).
2. Confirm the deletion.

> **Warning:** Deleting a buyer also deletes their login account. Any samples linked to this buyer will remain but will have no buyer assigned.

---

## 9. Brands

Brands represent the product labels or customer brands that samples belong to.

> **Who can manage brands:** Super Admin (create/edit/delete). Top Management and General Customer can view only.

### Viewing Brands

Click **Brands** under the Lookups section. The list shows the brand name, origin country (with flag), and the number of samples associated with each brand.

### Adding a Brand

1. Click **Add Brand**.
2. Fill in:
   - **Brand Name** — Required
   - **Origin Country** — Select from the dropdown list of countries (optional)
   - **Brand Logo** — Upload an image file (optional; auto-compressed to 400px)
3. Click **Save**.

### Editing / Deleting a Brand

Use the **pencil** (✏️) or **trash** (🗑) icons on the Brand list. Confirm deletion when prompted.

---

## 10. Categories

Categories classify samples into product types (e.g. Tops, Bottoms, Accessories).

> **Who can manage categories:** Super Admin only. Top Management and General Customer can view only.

### Managing Categories

1. Click **Categories** under the Lookups section.
2. Use **Add Category** to create a new one — enter the category name and click **Save**.
3. Use the **pencil** (✏️) to edit a name, or the **trash** (🗑) to delete.

Use the **search box** at the top to find a specific category quickly.

---

## 11. GGs

GGs are a technical lookup value used to classify gauge or grade information on samples.

> **Who can manage GGs:** Super Admin only. Top Management and General Customer can view only.

### Managing GGs

1. Click **GGs** under the Lookups section.
2. Use **Add GG** to create a new one — enter the GG title and click **Save**.
3. Use the **pencil** (✏️) or **trash** (🗑) icons to edit or delete.

---

## 12. Challenges In

"Challenges In" records the types of issues or challenges identified during sample evaluation (e.g. Stitching Issue, Color Mismatch, Size Problem).

> **Who can manage Challenges In:** Super Admin only. Top Management and General Customer can view only.

### Managing Challenges In

1. Click **Challenges In** under the Lookups section.
2. Use **Add Challenge** to create a new entry — enter the title and click **Save**.
3. Use the **pencil** (✏️) or **trash** (🗑) icons to edit or delete.

---

## 13. Top Management Accounts

Top Management accounts are for executives and leadership who need full visibility into all data without being able to modify anything.

> **Who can manage Top Management accounts:** Super Admin only.

### Viewing Top Management Members

Click **Top Management** under the Management section in the sidebar (visible to Super Admin only).

The list shows each member's name, username, department, and designation.

### Adding a Top Management Account

1. Click **Add Member**.
2. Fill in:

| Field | Description |
|---|---|
| **Username** | Login username |
| **Password** | Initial login password |
| **Full Name** | Member's full name |
| **Department** | Department (e.g. Operations, Finance) |
| **Designation** | Job title (e.g. CEO, Director) |

3. Click **Save**.

### Editing / Deleting a Top Management Account

Use the **pencil** (✏️) or **trash** (🗑) icons on the list. When editing, leave **Password** blank to keep the existing one.

### What Top Management users can do

- View Dashboard with full system statistics
- View all Samples (list and detail)
- View all Makers and their profiles
- View all Buyers and their profiles
- View all Brands, Categories, GGs, and Challenges In
- Export samples to PDF or Excel

They **cannot** create, edit, or delete any data. Any attempt will show a "view-only access" message.

---

## 14. General Customer Accounts

General Customer accounts are similar to Top Management — full read-only visibility into all data. They are suited for external stakeholders or clients who need access without management responsibilities.

> **Who can manage General Customer accounts:** Super Admin only.

### Viewing General Customers

Click **General Customers** under the Management section in the sidebar (visible to Super Admin only).

### Adding a General Customer Account

1. Click **Add Customer**.
2. Fill in:

| Field | Description |
|---|---|
| **Username** | Login username |
| **Password** | Initial login password |

3. Click **Save**. (No additional profile fields are required.)

### Editing / Deleting a General Customer Account

Use the **pencil** (✏️) or **trash** (🗑) icons on the list.

### What General Customer users can do

Identical to Top Management — full read-only access to all pages and data. They **cannot** create, edit, or delete anything.

---

## 15. Role-by-Role Quick Reference

### Super Admin

| Feature | Access |
|---|---|
| Dashboard (all data) | ✅ |
| View all Samples | ✅ |
| Create / Edit / Delete Samples | ✅ |
| Export Samples | ✅ |
| View Makers | ✅ |
| Create / Edit / Delete Makers | ✅ |
| View Buyers | ✅ |
| Create / Edit / Delete Buyers | ✅ |
| Manage Brands | ✅ |
| Manage Categories | ✅ |
| Manage GGs | ✅ |
| Manage Challenges In | ✅ |
| Manage Top Management accounts | ✅ |
| Manage General Customer accounts | ✅ |

---

### Maker

| Feature | Access |
|---|---|
| Dashboard (own samples only) | ✅ |
| View Samples (assigned to them) | ✅ |
| Create / Edit / Delete Samples | ✅ |
| Export Samples | ✅ |
| Update own Profile Picture | ✅ |
| View Buyers / Makers | ❌ |
| Manage any Lookup data | ❌ |
| Manage any User accounts | ❌ |

---

### Buyer

| Feature | Access |
|---|---|
| Dashboard (own brand samples) | ✅ |
| View Samples (own brands only) | ✅ |
| View Sample Details (own brands only) | ✅ |
| Export Samples (own brands) | ✅ |
| Create / Edit / Delete anything | ❌ |
| View Makers or other Buyers | ❌ |
| Manage Lookup data | ❌ |

---

### Top Management

| Feature | Access |
|---|---|
| Dashboard (all data) | ✅ View only |
| View all Samples | ✅ View only |
| Export Samples | ✅ |
| View all Makers | ✅ View only |
| View all Buyers | ✅ View only |
| View Brands / Categories / GGs / Challenges | ✅ View only |
| Create / Edit / Delete anything | ❌ |
| Manage any User accounts | ❌ |

---

### General Customer

| Feature | Access |
|---|---|
| Dashboard (all data) | ✅ View only |
| View all Samples | ✅ View only |
| Export Samples | ✅ |
| View all Makers | ✅ View only |
| View all Buyers | ✅ View only |
| View Brands / Categories / GGs / Challenges | ✅ View only |
| Create / Edit / Delete anything | ❌ |
| Manage any User accounts | ❌ |

---

## 16. Frequently Asked Questions

**Q: I can't log in — what should I do?**
Make sure you are using the correct username and password (they are case-sensitive). If you have forgotten your credentials, contact your Super Admin to reset your password.

---

**Q: I can see a page but the Add / Edit / Delete buttons are missing — is this a bug?**
No. This is intentional. If you are logged in as Top Management or General Customer, you have view-only access and those buttons are hidden. Contact your Super Admin if you need write access.

---

**Q: I tried to save a form and got a "view-only access" error — why?**
Your role does not allow making changes. Even if you navigate directly to a create/edit URL, the system will block the action and return you to the previous page.

---

**Q: As a Buyer, why can I only see some samples?**
Buyer accounts are restricted to samples belonging to the brands assigned to their account. If you believe you should be seeing more samples, contact your Super Admin to check your brand assignments.

---

**Q: How do I change my password?**
Your password can only be changed by the Super Admin. Contact them and they will update it for you from the edit page of your account.

---

**Q: I uploaded a large image but it looks smaller — is this correct?**
Yes. The system automatically compresses and resizes images on upload to optimise storage and page load speed. This is by design and does not affect image quality significantly.

---

**Q: What file types can I upload for documents?**
The documents field accepts any file type (PDF, Word, Excel, ZIP, etc.). Images (front part, back part, tech pack, challenge images) should be uploaded as JPG or PNG files.

---

**Q: Can I export all samples at once?**
The export function exports the samples on the **current page** (up to 10 at a time). To export a larger set, use the search and filter controls to narrow down exactly what you need, then export.

---

**Q: The brand logo isn't showing up in my navigation bar — what's wrong?**
Brand logos appear in the top navigation for Buyer accounts only, and only if a logo has been uploaded for that brand. Ask your Super Admin to upload the brand logo from the Brands section.

---

**Q: I deleted something by mistake — can it be recovered?**
No. All deletions in Trecelo are permanent. Always confirm carefully before clicking **Confirm Delete**. If you deleted a user account (maker, buyer, etc.), it will need to be recreated from scratch by the Super Admin.

---

*For further assistance, contact your system Super Admin.*
