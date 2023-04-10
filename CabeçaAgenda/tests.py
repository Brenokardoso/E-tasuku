from django.test import TestCase

# Create your tests here.




<a href="#content-start" class="skip-to-content-link">Skip to main content</a>
<!-- Container -->
<div id="container">

    
    <!-- Header -->
    
    <div id="header">
        <div id="branding">
        
<h1 id="site-name"><a href="/admin/">Django administration</a></h1>


        </div>
        
        
        <div id="user-tools">
            
                Welcome,
                <strong>brnomort</strong>.
            
            
                
                    <a href="/">View site</a> /
                
                
                    
                    
                
                
                <a href="/admin/password_change/">Change password</a> /
                
                <form id="logout-form" method="post" action="/admin/logout/">
                    <input type="hidden" name="csrfmiddlewaretoken" value="kQfwi4uuiXAQQQe98jP44qhKhZVeRboatSKXalln9K5jxldyCzyuk6EK3Dr9c7p9">
                    <button type="submit">Log out</button>
                </form>
                
<button class="theme-toggle">
  <div class="visually-hidden theme-label-when-auto">Toggle theme (current theme: auto)</div>
  <div class="visually-hidden theme-label-when-light">Toggle theme (current theme: light)</div>
  <div class="visually-hidden theme-label-when-dark">Toggle theme (current theme: dark)</div>
  <svg aria-hidden="true" class="theme-icon-when-auto">
    <use xlink:href="#icon-auto"></use>
  </svg>
  <svg aria-hidden="true" class="theme-icon-when-dark">
    <use xlink:href="#icon-moon"></use>
  </svg>
  <svg aria-hidden="true" class="theme-icon-when-light">
    <use xlink:href="#icon-sun"></use>
  </svg>
</button>

            
        </div>
        
        
        
    </div>
    
    <!-- END Header -->
    
      <nav aria-label="Breadcrumbs">
        
<div class="breadcrumbs">
<a href="/admin/">Home</a>
› <a href="/admin/Cabe%C3%A7aAgenda/">Cabeçaagenda</a>
› Tarefass
</div>

      </nav>
    
    

    <div class="main shifted" id="main">
      
        
          
<button class="sticky toggle-nav-sidebar" id="toggle-nav-sidebar" aria-label="Toggle navigation"></button>
<nav class="sticky" id="nav-sidebar" aria-label="Sidebar" aria-expanded="true">
  <input type="search" id="nav-filter" placeholder="Start typing to filter…" aria-label="Filter navigation items">
  


  
    <div class="app-auth module">
      <table>
        <caption>
          <a href="/admin/auth/" class="section" title="Models in the Authentication and Authorization application">Authentication and Authorization</a>
        </caption>
        
          <tbody><tr class="model-group">
            
              <th scope="row"><a href="/admin/auth/group/">Groups</a></th>
            

            
              <td><a href="/admin/auth/group/add/" class="addlink">Add</a></td>
            

            
          </tr>
        
          <tr class="model-user">
            
              <th scope="row"><a href="/admin/auth/user/">Users</a></th>
            

            
              <td><a href="/admin/auth/user/add/" class="addlink">Add</a></td>
            

            
          </tr>
        
      </tbody></table>
    </div>
  
    <div class="app-CabeçaAgenda module current-app">
      <table>
        <caption>
          <a href="/admin/Cabe%C3%A7aAgenda/" class="section" title="Models in the Cabeçaagenda application">Cabeçaagenda</a>
        </caption>
        
          <tbody><tr class="model-tarefas current-model">
            
              <th scope="row"><a href="/admin/Cabe%C3%A7aAgenda/tarefas/" aria-current="page">Tarefass</a></th>
            

            
              <td><a href="/admin/Cabe%C3%A7aAgenda/tarefas/add/" class="addlink">Add</a></td>
            

            
          </tr>
        
      </tbody></table>
    </div>
  


</nav>

        
      
      <div id="content-start" class="content" tabindex="-1">
        
          
        
        <!-- Content -->
        <div id="content" class="">
          
          <h1>Select tarefas to change</h1>
          
          
  <div id="content-main">
    
        <ul class="object-tools">
          
            


  
  <li>
    
    <a href="/admin/Cabe%C3%A7aAgenda/tarefas/add/" class="addlink">
      Add tarefas
    </a>
  </li>
  


          
        </ul>
    
    
    <div class="module filtered" id="changelist">
      <div class="changelist-form-container">
        

<div id="toolbar"><form id="changelist-search" method="get">
<div><!-- DIV needed for valid HTML -->
<label for="searchbar"><img src="/static/admin/img/search.svg" alt="Search"></label>
<input type="text" size="40" name="q" value="" id="searchbar">
<input type="submit" value="Search">


</div>

</form></div>


        

        <form id="changelist-form" method="post" novalidate=""><input type="hidden" name="csrfmiddlewaretoken" value="kQfwi4uuiXAQQQe98jP44qhKhZVeRboatSKXalln9K5jxldyCzyuk6EK3Dr9c7p9">
        

        
          
<div class="actions">
  
    
    <label>Action: <select name="action" required="">
  <option value="" selected="">---------</option>

  <option value="delete_selected">Delete selected tarefass</option>

</select></label><input type="hidden" name="select_across" value="0" class="select-across">
    
    
    <button type="submit" class="button" title="Run the selected action" name="index" value="0">Go</button>
    
    
    
        <span class="action-counter" data-actions-icnt="1">0 of 1 selected</span>
        
    
    
  
</div>

          


<div class="results">
<table id="result_list">
<thead>
<tr>

<th scope="col" class="action-checkbox-column">
   
   <div class="text"><span><input type="checkbox" id="action-toggle"></span></div>
   <div class="clear"></div>
</th>
<th scope="col" class="sortable column-tasks">
   
   <div class="text"><a href="?o=1">Tasks</a></div>
   <div class="clear"></div>
</th>
<th scope="col" class="sortable column-tasks_time">
   
   <div class="text"><a href="?o=2">Data da tarefa</a></div>
   <div class="clear"></div>
</th>
<th scope="col" class="column-foi_publicado">
   
   <div class="text"><span>Foi publicado</span></div>
   <div class="clear"></div>
</th>
</tr>
</thead>
<tbody>


<tr><td class="action-checkbox"><input type="checkbox" name="_selected_action" value="1" class="action-select"></td><th class="field-tasks"><a href="/admin/Cabe%C3%A7aAgenda/tarefas/1/change/">Arrumar essa interface de merda que ficou</a></th><td class="field-tasks_time nowrap">April 10, 2023, 2:30 a.m.</td><td class="field-foi_publicado">True</td></tr>

</tbody>
</table>
</div>


          
        
        

<p class="paginator">

1 tarefas


</p>

        </form>
      </div>
      
        
          <div id="changelist-filter">
            <h2>Filter</h2>
            
            
<details data-filter-title="Data da tarefa" open="">
  <summary>
     By Data da tarefa 
  </summary>
  <ul>
  
    <li class="selected">
    <a href="?">Any date</a></li>
  
    <li>
    <a href="?tasks_time__gte=2023-04-10+00%3A00%3A00%2B00%3A00&amp;tasks_time__lt=2023-04-11+00%3A00%3A00%2B00%3A00">Today</a></li>
  
    <li>
    <a href="?tasks_time__gte=2023-04-03+00%3A00%3A00%2B00%3A00&amp;tasks_time__lt=2023-04-11+00%3A00%3A00%2B00%3A00">Past 7 days</a></li>
  
    <li>
    <a href="?tasks_time__gte=2023-04-01+00%3A00%3A00%2B00%3A00&amp;tasks_time__lt=2023-05-01+00%3A00%3A00%2B00%3A00">This month</a></li>
  
    <li>
    <a href="?tasks_time__gte=2023-01-01+00%3A00%3A00%2B00%3A00&amp;tasks_time__lt=2024-01-01+00%3A00%3A00%2B00%3A00">This year</a></li>
  
  </ul>
</details>

          </div>
        
      
    </div>
  </div>

          
          <br class="clear">
        </div>
        <!-- END Content -->
        <div id="footer"></div>
      </div>
    </div>
</div>
<!-- END Container -->

<!-- SVGs -->
<svg xmlns="http://www.w3.org/2000/svg" class="base-svgs">
  <symbol viewBox="0 0 24 24" width="1rem" height="1rem" id="icon-auto"><path d="M0 0h24v24H0z" fill="currentColor"></path><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2V4a8 8 0 1 0 0 16z"></path></symbol>
  <symbol viewBox="0 0 24 24" width="1rem" height="1rem" id="icon-moon"><path d="M0 0h24v24H0z" fill="currentColor"></path><path d="M10 7a7 7 0 0 0 12 4.9v.1c0 5.523-4.477 10-10 10S2 17.523 2 12 6.477 2 12 2h.1A6.979 6.979 0 0 0 10 7zm-6 5a8 8 0 0 0 15.062 3.762A9 9 0 0 1 8.238 4.938 7.999 7.999 0 0 0 4 12z"></path></symbol>
  <symbol viewBox="0 0 24 24" width="1rem" height="1rem" id="icon-sun"><path d="M0 0h24v24H0z" fill="currentColor"></path><path d="M12 18a6 6 0 1 1 0-12 6 6 0 0 1 0 12zm0-2a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM11 1h2v3h-2V1zm0 19h2v3h-2v-3zM3.515 4.929l1.414-1.414L7.05 5.636 5.636 7.05 3.515 4.93zM16.95 18.364l1.414-1.414 2.121 2.121-1.414 1.414-2.121-2.121zm2.121-14.85l1.414 1.415-2.121 2.121-1.414-1.414 2.121-2.121zM5.636 16.95l1.414 1.414-2.121 2.121-1.414-1.414 2.121-2.121zM23 11v2h-3v-2h3zM4 11v2H1v-2h3z"></path></symbol>
</svg>
<!-- END SVGs -->


