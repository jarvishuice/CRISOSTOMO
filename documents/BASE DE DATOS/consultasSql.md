1.
```sql
/**********************************************************************                                                                   
 * acutalizacion de de la cantidad de lbros publicados segun su autor *
 *                                                                    *
 **********************************************************************/
update autores set cantidad_libros = (select count(id) from libros where 
                                id_autor = '1' ) where id='1' ; 
```
2.
``` sql 

/***********************************************************************
 * Reacciones detallasdas nombre de usuario y de autor                 *
 *                                                                     *
 ***********************************************************************/                               
select  l.titulo as libro , u.user_name as USUARIO , r.fecha from 
reacciones r 
inner join libros l on l.titulo = l.titulo
inner join "user" u on u.user_name = user_name 
where u.ci = r.id_user and l.id = r.id_libro 
order by r.fecha  desc
```