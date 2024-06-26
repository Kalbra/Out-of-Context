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

window.onload = function() {
  fetchTeachersFromUrl();
};