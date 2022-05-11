/** HTML Table Sort
 * 
 * @param {HTMLTableElement} table The table will be sorted
 * @param {number} column The number of column will be sorted
 * @param {boolean} asc Determine if the sorted will be ascendent or descendent
 */

function sortTableByColumn(table, column, asc= true){
    dirModify = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll('tr'));




    //Sorting the rows
    const sortedRows = rows.sort((a, b) =>{
        if (column != 0){

            aColText = parseInt(a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim());
            bColText = parseInt(b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim());
        }
        else{
            aColText = a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();
            bColText = b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();
        }

       return aColText > bColText? (1 * dirModify) : (-1 * dirModify);
    });


    //Remove TRs by the table
    while (tBody.firstChild){
        tBody.removeChild(tBody.firstChild);
    }

    //Addition the new rows sorted in table
    tBody.append(...sortedRows);

    //Remember the currently sorted column
    table.querySelectorAll('th').forEach(th => th.classList.remove('th-sorted-asc', 'th-sorted-desc'));
    table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle('th-sorted-asc', asc);
    table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle('th-sorted-desc', !asc);
}


document.querySelectorAll('.table-sortable th').forEach(headerCell =>{
    headerCell.addEventListener('click', () =>{
        const tableElement = headerCell.parentElement.parentElement.parentElement;
        const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
        const currentlyIsAscending = headerCell.classList.contains('th-sorted-asc');

        sortTableByColumn(tableElement, headerIndex, !currentlyIsAscending);
    })
})