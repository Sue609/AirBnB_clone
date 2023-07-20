HTML(Hypertext Markup Language) is the standard markup language used to staracture and organize the content of web pages. It provides a set of tags that define the stucture and semantics of the content on a web page. HTML elements represent different parts of a web page, such as headings, paragraphs, images, links, forms, and more. When a web browser reads an HTML document, it interprets the markup and renders the content accordingly.
The key features: 
1. Tags
2. Nesting
3. Attributes
4. Semantic Markup

CSS is a stylesheet language used to define the representation and layout of HTML documents. It separates the content from its visual representation.  With CSS, you can apply styles such as colors, fonts, spacing, positioning, and more to HTML elements, allowing you to control the appearance of a web page.
Key features:
1. Selectors
2. Properties.
3. Values
4. Cascading and Specificity.

- In this project we shall be looking at the introduction of HTML & CSS basic syntax and learn the ropes of how they operate. We shall be looking at:
0. Writing a HTML page that display a header and a footer.
1. Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)
2. Write an HTML page that displays a header and a footer by using CSS files 
Requirements:
    You must use the header and footer tags
    No inline styling
    You must have 3 CSS files:
    styles/2-common.css: for global style (i.e. the body style)
    styles/2-header.css: for header style
    styles/2-footer.css: for footer style
3. Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)
Layout:
    Common:
        no margin
        no padding
        font color: #484848
        font size: 14px
        font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
        icon in the browser tab
    Header:
        color: white
        height: 70px
        width: 100%
        border bottom 1px #CCCCCC
        logo align on left and center vertically (20px space at the left)
    Footer:
        color white
        height: 60px
        width: 100%
        border top 1px #CCCCCC
        text Best School center vertically and horizontally
        always at the bottom at the page
    Requirements:
        No inline style
        You are not allowed to use the img tag
        You are not allowed to use the style tag in the head tag
        All images must be stored in the images folder
        You must have 3 CSS files:
        styles/3-common.css: for the global style (i.e body style)
        styles/3-header.css: for the header style
        styles/3-footer.css: for the footer style

4. Write an HTML page that displays a header, footer and a filters box with a search button.
Layout: (based on 3-index.html)
    Container:
        between header and footer tags, add a div:
            classname: container
            max width 1000px
            margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
            center horizontally
    Filter section:
        tag section
        classname filters
        inside the .container
        color white
        height: 70px
        width: 100% of the container
        border 1px #DDDDDD with radius 4px
    Button search:
        tag button
        text Search
        font size: 18px
        inside the section filters
        background color #FF5A5F
        text color #FFFFFF
        height: 48px
        width: 20% of the section filters
        no borders
        border radius: 4px
        center vertically and at 30px of the right border
        change opacity to 90% when the mouse is on the button
Requirements:
    You must use: header, footer, section, button tags
    No inline style
    You are not allowed to use the img tag
    You are not allowed to use the style tag in the head tag
    All images must be stored in the images folder
    You must have 4 CSS files:
        styles/4-common.css: for the global style (body and .container styles)
        styles/3-header.css: for the header style
        styles/3-footer.css: for the footer style
        styles/4-filters.css: for the filters style
        4-index.html won’t be W3C valid, don’t worry, it’s temporary

5. Write an HTML page that displays a header, footer and a filters box.
Layout: (based on 4-index.html)
    Locations and Amenities filters:
    tag: div
    classname: locations for location tag and amenities for the other
    inside the section filters (same level as the button Search)
    height: 100% of the section filters
    width: 25% of the section filters
    border right #DDDDDD 1px only for the first left filter
    contains a title:
        tag: h3
        font weight: 600
        text States or Amenities
    contains a subtitle:
        tag: h4
        font weight: 400
        font size: 14px
        text with fake contents
Requirements:
    You must use: header, footer, section, button, h3, h4 tags
    No inline style
    You are not allowed to use the img tag
    You are not allowed to use the style tag in the head tag
    All images must be stored in the images folder
    You must have 4 CSS files:
    styles/4-common.css: for the global style (body and .container styles)
    styles/3-header.css: for the header style
    styles/3-footer.css: for the footer style
    styles/5-filters.css: for the filters style