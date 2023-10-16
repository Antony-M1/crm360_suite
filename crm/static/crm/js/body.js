
document.querySelectorAll('.sidebar a').forEach(link => {
    link.addEventListener('click', async function(event) {
        event.preventDefault();
        const apiEndpoint = this.getAttribute('data-api-endpoint');
        try {
            const response = await fetch(`/api/${apiEndpoint}/`);
            const data = await response.json();
            renderTable(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    });
});

function renderTable(data) {
    const table = document.getElementById('data-table');
    table.innerHTML = ''; // Clear existing content

    // Create table header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    Object.keys(data[0]).forEach(key => {
        const th = document.createElement('th');
        th.textContent = key;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement('tbody');
    data.forEach(row => {
        const tr = document.createElement('tr');
        Object.values(row).forEach(value => {
            const td = document.createElement('td');
            td.textContent = value;
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);
}
