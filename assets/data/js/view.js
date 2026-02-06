/*=============== SHOW SIDEBAR ===============*/
const showSidebar = (toggleId, sidebarId) => {
   const toggle = document.getElementById(toggleId),
         sidebar = document.getElementById(sidebarId)

   toggle.addEventListener('click', () => {
      sidebar.classList.toggle('show-sidebar')
   })
}
showSidebar('header-toggle','sidebar')

/*=============== SHOW SIDEBAR LIST ===============*/
const drop = document.querySelectorAll('.drop')

drop.forEach(item => {
   const dropBtn = item.querySelector('.drop__button'),
         dropList = item.querySelector('.drop__list')

   dropBtn.addEventListener('click', () => {
      // 2. Close any other drop that are open
      const openItem = document.querySelector('.show-drop') // Search if there are any open drop

      // Check if there is an open drop
      if (openItem && openItem !== item) {
         const openList = openItem.querySelector('.drop__list')
         openList.removeAttribute('style')
         openItem.classList.remove('show-drop')
      }

      // 1. Show drop list (Ask if the drop is open or closed)
      if (item.classList.contains('show-drop')) {
         // If it's OPEN → IT CLOSES
         dropList.removeAttribute('style')
         item.classList.remove('show-drop')
      } else {
         // If it's CLOSED → IT OPENS
         dropList.style.height = dropList.scrollHeight + 'px'
         item.classList.add('show-drop')
      }
   })
})

// 1. Define the JSON data as a JavaScript object
const myJSON = {
   affiliation: "friendly",
   symbol: "Default Land Unit",
   echelon: "none",
   mod1: "None",
   mod2: "None",
   uniqueDesignation: "Alpha Unit",
   location: {
         latitude: 34.0522,
         longitude: -118.2437
   }
};

// 2. Convert the JSON object to a nicely formatted string
// null is for a replacer function (optional), and 2 defines the number of spaces for indentation
const formattedJsonString = JSON.stringify(myJSON, null, 2);

// 3. Place the formatted string into the <pre> tag
document.getElementById("timestamps").innerText = formattedJsonString;
