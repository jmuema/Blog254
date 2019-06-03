# Techie Talk

This is a flask blog where a writer posts blogs and a user can view and comment on them

## Author Information
Written by *Joseph Muema*. My first attempt at interating psql into my flask app including an API

## Installation

1. Clone the repository
2. Create a virtual environment and install flask in your repository folder 
3. Run the IP address on the browser

## Site manuevering.
1. Click the link on my github description to manuever through the site as a user
2. Create a new writer account using this link to maneuver through the application as a writer:                                                https://thelastblog.herokuapp.com/authenticate/register
This will ensure only authorized writers can post blogs on the application

## Behaviour Driven Development

| Behavior our program should handle | Input description |  Output description
| --- | --- | --- |
| `View blog posts on the site` | None | Blogs displayed
| `Registration into the app` | Writer credentials |  Redirection to login form
| `View most recent blogs` | Blogs in separate form |  Arranged list of blogs
| `View random quotes` | None |  A random quote is displayed
| `Comments from a user` | Comment|  Comment along with user's name

### Contact Information

To reach me, email me at: > jmuema95@gmail.com

### License
MIT License

Copyright (c) [2019] [Joseph Muema]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.