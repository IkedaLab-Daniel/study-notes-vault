# Module 8: Communicate Using Markdown

## Unit 1: Introduction
Markdown allows you to organize and emphasize what you're trying to communicate on GitHub.

A markup language, Markdown offers a lean approach to content editing. It defines a concise, lightweight syntax that strips out the overhead inherent to HTML, providing a more approachable creation experience. It's become the standard for sites like GitHub, and enjoys broad editor support in both client and browser forms.

### Learning objectives
In this module, you'll:

- Use Markdown to add lists, images, and links in a comment or text file.
- Determine where and how to use Markdown in a GitHub repository.
- Learn about syntax extensions available in GitHub (GitHub-flavored Markdown).

## Unit 2: What is Markdown?
Markdown is a markup language that offers a lean approach to content editing by shielding content creators from the overhead of HTML. While HTML is great for rendering content exactly how it was intended, it takes up a lot of space and can be unwieldy to work with, even in small doses. Markdown offers a great compromise between the power of HTML for content description and the ease of plain text for editing.

### Emphasize text
The most important part of any communication on GitHub is usually the text itself, but how do you show that some parts of the text are more important than others?

Using italics in text is as easy as surrounding the target text with single asterisks (*) or single underscores (_). Just be sure to close an emphasis with the same character with which you opened it. Be observant of how you combine the use of asterisks and underscores. Here are several examples:

```bash
This is *italic* text.
This is also _italic_ text.
```

This is *italic* text.
This is also _italic_ text.

Create bold text by using two asterisks (**) or two underscores (__).

```bash
This is **bold** text.
This is also __bold__ text.
```

This is **bold** text.
This is also __bold__ text.

You can also mix different emphases.

```bash
_This is **italic and bold** text_ using a single underscore for italic and double asterisks for bold.
__This is bold and *italic* text__ using double underscores for bold and single asterisks for italic.
```

_This is **italic and bold** text_ using a single underscore for italic and double asterisks for bold.
__This is bold and *italic* text__ using double underscores for bold and single asterisks for italic.

To use a literal asterisk, precede it with an escape character; in GFM, that's a backslash (\). This example results in the underscores and asterisks being shown in the output.

```bash
\_This is all \*\*plain\*\* text\_.
```

\_This is all \*\*plain\*\* text\_.

### Declare headings
HTML provides content headings such as the <h1> tag. In Markdown, this is supported via the # symbol. Just use one # for each heading level from 1 to 6.

### Link to images and sites
Image and site links use a similar syntax.

```bash
![Link an image.](/learn/azure-devops/shared/media/mara.png)
```

![Link an image.](/learn/azure-devops/shared/media/mara.png)

```bash
[Link to Microsoft Training](/training)
```

[Link to Microsoft Training](/training)

### Make lists
You can define ordered or unordered lists. You can also define nested items through indentation.

- Ordered lists start with numbers.
- Unordered lists can use asterisks or dashes (-).
Here's the Markdown for an ordered list:

### Build tables
You can construct tables using a combination of pipes (|) for column breaks and dashes (-) to designate the prior row as a header.

```bash
First|Second
-|-
1|2
3|4
```

First|Second
-|-
1|2
3|4

### Quote text
You can create blockquotes using the greater than (>) character.

```bash
> This is quoted text.
```

> This is quoted text.

### Fill the gaps with inline HTML
If you come across an HTML scenario not supported by Markdown, you can use that HTML inline.

```bash
Here is a<br />line break
```

Here is a<br />line break

### Work with code
Markdown provides default behavior for working with inline code blocks delimited by the backtick (`) character. When decorating text with this character, it's rendered as code.

```bash
This is `code`.
```

This is `code`.

If you have a code segment spanning multiple lines, you can use three backticks (```) before and after to create a fenced code block.

```markdown
var first = 1;
var second = 2;
var sum = first + second;
```

### Cross-link issues and pull requests
GFM supports various shortcode formats to make it easy to link to issues and pull requests. The easiest way to do this is to use the format #ID, such as #3602. GitHub automatically adjusts longer links to this format if you paste them in. There are also additional conventions you can follow, such as if you're working with other tools or want to specify other projects/branches.

### Link specific commits
You can link to a commit by either pasting in its ID or simply using its secure hash algorithm (SHA).

### Mention users and teams
Typing an @ symbol followed by a GitHub username sends a notification to that person about the comment. This is called an "@mention", because you're mentioning the individual. You can also @mention teams within an organization.

```bash
@githubteacher
```

@githubteacher

### Track task lists
You can create task lists within issues or pull requests using the following syntax. These can be helpful to track progress when used in the body of an issue or pull request.

```markdown
- [x] First task
- [x] Second task
- [ ] Third task
```

- [x] First task
- [x] Second task
- [ ] Third task

### Slash commands
Slash commands can save you time by reducing the typing required to create complex Markdown.

You can use slash commands in any description or comment field in issues, pull requests, or discussions where that slash command is supported.

## Unit 3: Lab
## Unit 4: Quiz
## Unit 5: Summary
