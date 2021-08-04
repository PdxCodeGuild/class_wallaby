# Accessibility

Accessibility is the practice of making your websites usable by as many people as possible. We traditionally think of this as being about people with disabilities, but the practice of making sites accessible also benefits other groups such as those using mobile devices, or those with slow network connections.

When you're building an accessible website, you want to keep in mind the following:

- Include semantic HTML, which improves accessibility, also improves SEO, making your site more findable.
- Caring about accessibility demonstrates good ethics and morals, which improves your public image.
- Other good practices that improve accessibility also make your site more usable by other groups, such as mobile phone users or those on low network speed. In fact, everyone can benefit from many such improvements.

Read more about accessibility [here](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/What_is_accessibility)

Here's an example of a fairly accessible site with semantically meaninful HTML:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My awesome website</title>
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li>Home</li>
          <li>About</li>
        </ul>
      </nav>
    </header>
    <main>
      <section>
        <h2>Introduction</h2>
        <p>
          This document provides a guide to help with the important task of
          choosing the correct Apple.
        </p>
      </section>

      <section>
        <h2>Criteria</h2>
        <p>
          There are many different criteria to be considered when choosing an
          Apple — size, color, firmness, sweetness, tartness...
        </p>
      </section>
    </main>
  </body>
</html>
```

Here's an example of a poorly accessible site:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My awesome website</title>
  </head>
  <body>
    <div>
      <div>
        <div>
          <div>Home</div>
          <div>About</div>
        </div>
      </div>
    </div>
    <div>
      <div>
        <div>Introduction</div>
        <div>
          This document provides a guide to help with the important task of
          choosing the correct Apple.
        </div>
      </div>

      <div>
        <div>Criteria</div>
        <div>
          There are many different criteria to be considered when choosing an
          Apple — size, color, firmness, sweetness, tartness...
        </div>
      </div>
    </div>
  </body>
</html>
```