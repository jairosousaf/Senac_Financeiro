




<div class='contas'>
                    {% for conta in contas %}
                        <div class="lista-contas-main">
                             <span><img width="10%" src="{{conta.icone.url}}">&nbsp&nbsp{{conta}}</span>
               
                             <span class="total-conta positivo ">R$ {{conta.valor}}<a href="/perfil/deletar_banco/{{conta.id}}"><img src="{% static '/perfil/img/exit.png' %}"></a>
                         </div>
                         <br>
                    {% endfor %}
               </div>
               
<div class='contas'>
                    {% for conta in contas %}
                        <div class="lista-contas-main">
                             <span><img width="10%" src="{{conta.icone.url}}">{{conta}}</span>
               
                             <span class="total-conta positivo ">R$ {{conta.valor}}<a href="perfil/deletar_banco/{{conta.id}}"><img src="{% static 'perfil/img/exit.png' %}"></a></span>
                         </div>
                         <br>
                    {% endfor %}
               </div>
               
<div class='contas'>
                    {% for conta in contas %}
                        <div class="lista-contas-main">
                             <span><img width="10%" src="{{conta.icone.url}}">&nbsp&nbsp{{conta}}</span>
               
                             <span class="total-conta positivo ">R$ {{conta.valor}}<a href="/perfil/deletar_banco/{{conta.id}}"><img src="{% static '/perfil/img/exit.png' %}"></a>
                         </div>
                         <br>
                    {% endfor %}
               </div>