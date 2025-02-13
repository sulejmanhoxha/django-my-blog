// const darkmode_button = document.getElementById("darkmode-button");
// darkmode_button.addEventListener("click", () => {
//   document.documentElement.classList.toggle("dark");
// });

const darkmode_button = document.getElementById("darkmode-button");
const html_tag = document.documentElement;
const theme = localStorage.getItem("theme");

if (theme) {
  html_tag.classList.add(theme);
}

darkmode_button.addEventListener("click", () => {
  html_tag.classList.toggle("dark");
  const theme = html_tag.classList.contains("dark") ? "dark" : "";
  localStorage.setItem("theme", theme);
});
