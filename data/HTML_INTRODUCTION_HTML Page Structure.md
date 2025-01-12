
# HTML Page Structure

An HTML document is structured using a set of nested tags. Each tag is enclosed within `<�>`  angle brackets and acts as a container for content or other HTML tags. Let's take a look at a basic HTML document structure:

```markup
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
</head>
<body>
   <!-- content -->
</body>
</html>

```


This is how the title appears on an HTML page:

A typical HTML page looks like this:

| Element       | Content/Description          |
|---------------|-------------------------------|
| `<html>`      | Root element of an HTML document. |
| `<head>`      | Contains metadata and links.   |
| `<title>`     | Page title: "Page title".      |
| `<body>`      | Main content of the HTML document. |
| `<h1>`        | A heading: "This is a heading". |
| `<p>`         | A paragraph: "This is a paragraph." |
| `<p>`         | Another paragraph: "This is another paragraph." |


Almost every website uses this structure. The main content goes inside the body tag. No worries if this looks complicated; let's break it down!

**Note:**  These are the essential elements for a basic HTML document: **`<!DOCTYPE html>`,  `<html>`,  `<head>`,  `<title>`,  `</head>`,  `<body>`,  `</body>`,  `</html>`**

### DOCTYPE Declaration

```markup
<!DOCTYPE html>
```


The  `<!DOCTYPE html>`  declaration informs the web browser about the HTML version being used. The latest version is HTML5. But if this changes in the future (maybe 10 years down the line), the doctype declaration will be helpful!

### HTML Root Element

```markup
<html>
```


The  `<html>`  tag is the root element that encapsulates all the content on the page.

```markup
</html>
```


The `</html>`  tag marks the end of the  `<html>`  section.

### Head Section

```markup
<head>
```


The  `<head>`  tag contains metadata and links to external resources like CSS and JavaScript files.

```markup
</head>
```


The  `</head>`  tag marks the end of the  `<head>`  section.

### Title Tag

```markup
<title>Document</title>
```


The  `<title>`  tag sets the title of the web page, which is displayed in the browser's title bar or tab.

### Body Tag

```markup
<body>
```


The  `<body>`  tag contains the visible content of the web page. This is where text, images, and other elements go.

```markup
</body>
```



The  `</body>`  tag marks the end of the visible content of the web page.

Every HTML page should include at least these essential elements to define the basic layout. In upcoming tutorials, we'll dive deeper into the fascinating world of HTML.

## Summary

-   The  `<!DOCTYPE html>`  tag specifies that the document is an HTML5 document.
-   The  `<html lang="en">`  tag defines the document to be in English.
-   The  `<head>`  section contains metadata and the title of the webpage, which appears in the browser's title bar.
-   The  `<body>`  section contains the content that will be displayed on the webpage.
-   The h1 and p are two types of tags. We will learn about more tags in the later section

### **Visualization of an HTML Document:**

The following image provides a visual representation of the HTML structure:

![cwh tutorial image](https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/tutorial/html-page-structure/html-tag-structure-image.png)

### **How This Content Appears in a Web Browser:**

Consider this html code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
</head>
<body>
    <h1> This is a heading</h1>
    <p>This is a paragraph</p>
</body>
</html>

```


Below is an image showing how this HTML document will be rendered in a web browser:

![cwh tutorial image](https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/tutorial/html-page-structure/html-headings.png)

In the browser, the title bar will display the content from the  `<head>`  section, specifically the  `<title>`  tag. The main area of the browser window (usually a white background) will display the content inside the  `<body>`  tag.

In the upcoming sections, we will learn about html tags and elements.

