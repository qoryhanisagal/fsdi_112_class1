# FSDI_112 Learning Journey: Organizo(Tiimo) Login & About Page Project

## Overview

This project represents my learning journey through Django web development as part of the FSDI_112 course. I built a login page and a personalized About page, styled with CSS, and structured using Django templates. Along the way, I encountered real-world issues and had to troubleshoot through some major roadblocks.

---

## Learning Highlights

### ✅ What I Accomplished
- Built a dynamic login page using Django's template engine and custom CSS
- Created a personalized "About the Developer" page with social media links and CTA elements
- Used Bootstrap and Bootstrap Icons to add styling and consistency
- Learned how to structure Django projects with `static`, `templates`, and `apps`
- Practiced Git commands instead of relying on GUI features to understand project flow

---

## 🧩 Login Page, About Page & Navbar Struggles

One area where I spent a lot of energy was designing the login page. A big challenge came from the **navbar** — it was part of the `base.html` file the instructor gave us, but it didn’t align with my design vision. I didn’t want the login page to include a navbar, especially one with full navigation links. It just felt out of place.

I tried to work around this by conditionally removing the navbar using logic in my templates, but that approach didn’t work as expected. In hindsight, I realized I might have been better off **including a navbar manually on each page** that needs it, or designing simplified navbars for specific pages like the About page, where I don’t want users to navigate away.

Even though we worked on a homepage as part of the project, I kept mine very basic. I didn’t invest as much into styling it because I was focused on the login and about pages. While the login page itself doesn’t use unique styling, I learned how to structure the layout using Django’s template engine and organize my CSS files cleanly.

The About page, on the other hand, became a great opportunity to express design through layout, image handling, and icon usage — even integrating the “Buy Me a Coffee” button and social links under the image and text.

---

## 😓 Biggest Challenge: Renaming `message_board` to `config`

One of the biggest obstacles I faced was **renaming my Django project folder** from `message_board` to `config`. I didn't realize how tightly Django binds the project name to the settings and routing system. After renaming the folder, **everything broke** — and I was hit with endless `ModuleNotFoundError` and `ImportError` messages.

I had to manually go through every file — `asgi.py`, `wsgi.py`, `urls.py`, and `settings.py` — and **replace all references to `message_board` with `config`**. It was tedious and extremely frustrating, and it cost me **half of the class session** just to get my project back up and running.

---

## 🧠 Prep Work and Unexpected Curveballs

I take prep seriously. Before Monday's class, I read up on the topics and practiced tutorials from different sites. I thought I was prepared. But when we received our in-class **mini challenge**, things went sideways.

> The challenge wasn’t the functionality — it was the setup.

My project wasn't structured in a way that allowed me to jump in. I spent too much time fixing errors instead of learning the new material. I also tried to follow along using **Git CLI commands** like `mkdir`, `touch`, and `git add`, instead of just clicking through the interface. That made me a bit slower, but it’s how I learn.

---

## 📝 My Learning Process

Here’s how I typically learn in class:
- I **listen first**, then take handwritten notes to process what’s being said.
- Then I **type out** commands to reinforce the logic.
- The professor starts strong with breakdowns and recaps, which is great — but the class **moves fast** and I need time to think through each step.

Today, I felt like I was failing even though I was trying to do everything right. But reflecting on it now, I realize that:
- I **didn't fail** — I learned a lot about how Django projects work under the hood.
- I know how to fix module pathing errors and structure a project from scratch.

---

## ✅ Moving Forward

To better prepare for these challenges, I’ve created a **`practice_challenges/` folder inside my `sdgku_work` directory** where I can quickly scaffold and test out mini projects. This will help me stay aligned with the pace of the class while still learning the underlying logic.

---

## 💡 Takeaway

I may move slower than others, but I value **understanding over speed**. This project taught me to anticipate structure issues, lean on documentation, and troubleshoot methodically. And that’s what being a real developer is all about.

---

## 📁 Repository

This project is part of my GitHub repository [Organizo(Tiimo) Login & About Project](hhttps://github.com/qoryhanisagal/fsdi_112_class1)  

---
