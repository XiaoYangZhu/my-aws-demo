from nova_act import NovaAct

#with NovaAct(starting_page="https://www.amazon.com") as nova:
with NovaAct(starting_page="https://cn.bing.com/") as nova:    
    nova.act("search for a coffee maker")
    nova.act("select the first result")
    nova.act("scroll down or up until you see 'add to cart' and then click 'add to cart'")