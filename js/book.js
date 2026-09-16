const books = [
    "TEST"
];

const container = document.querySelector("#books");
const p = container.querySelector("p");

books.forEach(book => {
    const span = document.createElement("span");
    
    const link = document.createElement("a");
    link.href = `/posts/books_reading#${book}`;

    const image = document.createElement("img");
    image.src = `https://nothenrymoon.github.io/posts/books/${book}/cover.jpg`;
    image.width = 127;
    image.height = 201;
    image.alt = book;
    
    link.appendChild(image);
    span.appendChild(link);
    p.appendChild(span);
});