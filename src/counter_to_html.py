from collections import Counter
from IPython.display import display, HTML

def counter_to_html_table(counter, initial_visible=5):
    # Generar el HTML
    html = f"""
    <style>
        table {{
            width: 50%;
            margin: 20px auto;
            border-collapse: collapse;
            box-shadow: 0 5px 10px rgba(0,0,0,0.1);
        }}
        table, th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
        #filterInput {{
            width: 50%;
            margin: 20px auto;
            padding: 10px;
            border: 1px solid #ddd;
            font-size: 16px;
        }}
        .show-more-btn {{
            width: 50%;
            margin: 10px auto;
            text-align: center;
            cursor: pointer;
            color: #007bff;
            text-decoration: underline;
        }}
    </style>
    
    <input type="text" id="filterInput" onkeyup="filterTable()" placeholder="Buscar por elemento...">
    
    <table id="counterTable">
        <thead>
            <tr>
                <th>Elemento</th>
                <th>Conteo</th>
            </tr>
        </thead>
        <tbody>
    """
    # Añadir filas a la tabla con los datos del Counter
    for i, (item, count) in enumerate(counter.items()):
        style = "" if i < initial_visible else "display: none;"
        html += f'<tr style="{style}" class="table-row"><td>{item}</td><td>{count}</td></tr>'
    
    html += """
        </tbody>
    </table>
    
    <div id="showMoreBtn" class="show-more-btn" onclick="toggleRows()">Mostrar más...</div>
    
    <script>
    function filterTable() {{
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("filterInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("counterTable");
      tr = table.getElementsByTagName("tr");
      for (i = 1; i < tr.length; i++) {{
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {{
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {{
            tr[i].style.display = "";
          }} else {{
            tr[i].style.display = "none";
          }}
        }}       
      }}
    }}

    function toggleRows() {{
      var rows = document.getElementsByClassName("table-row");
      var showMoreBtn = document.getElementById("showMoreBtn");
      for (var i = 0; i < rows.length; i++) {{
        if (rows[i].style.display === "none") {{
          rows[i].style.display = "";
          showMoreBtn.innerText = "Mostrar menos...";
        }} else if (i >= {initial_visible}) {{
          rows[i].style.display = "none";
          showMoreBtn.innerText = "Mostrar más...";
        }}
      }}
    }}
    </script>
    """
    
    return html