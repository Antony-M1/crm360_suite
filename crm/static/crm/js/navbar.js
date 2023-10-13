function sideNavData(req){

    async function postJSON(data) {
        const loadData = document.getElementsByClassName("sidebar");
        try {
          const response = await fetch("http://127.0.0.1:8000/sidebar", {
            method: "POST", // or 'PUT'
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          });
          const result = await response.json();
          const sidebarContainer = document.getElementById('sidebar-container');
          sidebarContainer.innerHTML = ''; 
          for (let i=0;i<result.length;i++){
            
            console.log(result[i])
            const newLink = document.createElement('a');
            newLink.className = 'sidenav-link'
            newLink.href = '#';
            newLink.textContent = result[i].name
            sidebarContainer.appendChild(newLink);
   
          }
        } catch (error) {
          console.error("Error:", error);
        }
      }
      
      const data = {"type": req};
      postJSON(data);
      
}