async function fetchTeachersFromUrl() {
  try {
    const response = await fetch("/api/teacher_list");
    const data = await response.json();

    const selectElement = document.getElementById("teacher_list");
    selectElement.innerHTML = "";

    data.teachers.forEach((teacher) => {
      const option = document.createElement("option");
      option.value = teacher.id;
      option.textContent = teacher.teacher_name;
      selectElement.appendChild(option);
    });
  } catch (error) {
    console.error("Error fetching teacher data:", error);
  }
}

function SubmitQuote() {
  var quote_text = document.getElementById("quote_input").value;
  var teacher_id = document.getElementById("teacher_list").value;

  //@TODO: Check string


  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/api/new_quote", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          //var json = JSON.parse(xhr.responseText);
          //console.log(json.email + ", " + json.password);
      }
  };
  var data = JSON.stringify({"teacher_id": teacher_id, "quote": quote_text});
  console.log(data);
  xhr.send(data);
}

function createQuoteNode(author, text, votes) {
    // Create the outer container
    var commentContainer = document.createElement('div');
    commentContainer.className = 'comment-container';

    // Create the always-on-top div
    var alwaysOnTop = document.createElement('div');
    alwaysOnTop.className = 'always-on-top';

    // Create and append the image
    var img = document.createElement('img');
    img.src = 'images/blank-profile.webp';
    img.className = 'comment-image';
    alwaysOnTop.appendChild(img);

    // Create and append the author paragraph
    var authorParagraph = document.createElement('p');
    authorParagraph.className = 'comment-author';
    authorParagraph.innerText = author;
    alwaysOnTop.appendChild(authorParagraph);

    // Append always-on-top to the comment container
    commentContainer.appendChild(alwaysOnTop);

    // Create the always-on-bottom div
    var alwaysOnBottom = document.createElement('div');
    alwaysOnBottom.className = 'always-on-bottom';

    // Create and append the text paragraph
    var textParagraph = document.createElement('p');
    textParagraph.className = 'comment-text';
    textParagraph.innerText = text;
    alwaysOnBottom.appendChild(textParagraph);

    // Create and append the comment-votes div
    var commentVotes = document.createElement('div');
    commentVotes.className = 'comment-votes';

    // Create and append the thumbs up SVG
    var thumbsUpSVG = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    thumbsUpSVG.setAttribute('style', 'fill: limegreen;');
    thumbsUpSVG.setAttribute('viewBox', '0 0 32 32');
    thumbsUpSVG.innerHTML = '<path d="M27 11h-8.52L19 9.8A6.42 6.42 0 0 0 13 1a1 1 0 0 0-.93.63L8.32 11H5a3 3 0 0 0-3 3v14a3 3 0 0 0 3 3h18.17a3 3 0 0 0 2.12-.88l3.83-3.83a3 3 0 0 0 .88-2.12V14a3 3 0 0 0-3-3zM4 28V14a1 1 0 0 1 1-1h3v16H5a1 1 0 0 1-1-1zm24-3.83a1 1 0 0 1-.29.71l-3.83 3.83a1.05 1.05 0 0 1-.71.29H10V12.19l3.66-9.14a4.31 4.31 0 0 1 3 1.89 4.38 4.38 0 0 1 .44 4.12l-1 2.57A1 1 0 0 0 17 13h10a1 1 0 0 1 1 1z" data-name="thumb up android app aplication phone"></path>';
    commentVotes.appendChild(thumbsUpSVG);

    // Create and append the vote count div
    var voteCountDiv = document.createElement('div');
    voteCountDiv.className = 'vote-count';
    voteCountDiv.innerText = votes;
    commentVotes.appendChild(voteCountDiv);

    // Create and append the thumbs down SVG
    var thumbsDownSVG = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    thumbsDownSVG.setAttribute('style', 'fill: #c60000;');
    thumbsDownSVG.setAttribute('viewBox', '0 0 32 32');
    thumbsDownSVG.innerHTML = '<path d="m29.12 5.71-3.83-3.83A3 3 0 0 0 23.17 1H5a3 3 0 0 0-3 3v14a3 3 0 0 0 3 3h3.32l3.75 9.37A1 1 0 0 0 13 31a6.42 6.42 0 0 0 6-8.8l-.52-1.2H27a3 3 0 0 0 3-3V7.83a3 3 0 0 0-.88-2.12zM4 18V4a1 1 0 0 1 1-1h3v16H5a1 1 0 0 1-1-1zm24 0a1 1 0 0 1-1 1H17a1 1 0 0 0-.93 1.37l1 2.57a4.38 4.38 0 0 1-.44 4.12 4.31 4.31 0 0 1-3 1.89L10 19.81V3h13.17a1 1 0 0 1 .71.29l3.83 3.83a1 1 0 0 1 .29.71z" data-name="thumb down android app aplication phone"></path>';
    commentVotes.appendChild(thumbsDownSVG);

    // Append comment-votes to always-on-bottom
    alwaysOnBottom.appendChild(commentVotes);

    // Append always-on-bottom to the comment container
    commentContainer.appendChild(alwaysOnBottom);

    // Return the constructed comment container
    var comment = document.createElement("div");
    comment.classList.add("comment");
    comment.appendChild(commentContainer);
    return comment;
}

async function fetchQuotes() {
   try {
    const response = await fetch("/api/quote");
    const data = await response.json();

    data.quotes.forEach((quote) => {
      document.getElementById("container").
      appendChild(createQuoteNode(
          quote.teacher_name,
          quote.quote,
          quote.votes
      ));
    });
  } catch (error) {
    console.error("Error fetching quote data:", error);
  }
}

window.onload = function() {
  fetchTeachersFromUrl();
  fetchQuotes();
};