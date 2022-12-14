PGDMP     +    1            	    z        	   book_shop    14.5    14.5 "               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16394 	   book_shop    DATABASE     g   CREATE DATABASE book_shop WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Ukraine.1251';
    DROP DATABASE book_shop;
                postgres    false            ?            1259    16501    series    TABLE     ?   CREATE TABLE public.series (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    book_numbers integer NOT NULL,
    author_id integer NOT NULL
);
    DROP TABLE public.series;
       public         heap    postgres    false            ?            1259    16500    Series_series_id_seq    SEQUENCE     ?   ALTER TABLE public.series ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Series_series_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    212            ?            1259    16485    author    TABLE     a   CREATE TABLE public.author (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);
    DROP TABLE public.author;
       public         heap    postgres    false            ?            1259    16484    author_author_id_seq    SEQUENCE     ?   ALTER TABLE public.author ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.author_author_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    210            ?            1259    16522    book    TABLE     ?   CREATE TABLE public.book (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    price integer NOT NULL,
    amount integer NOT NULL,
    publication_date date NOT NULL,
    series_id integer NOT NULL
);
    DROP TABLE public.book;
       public         heap    postgres    false            ?            1259    16539 
   book_genre    TABLE     `   CREATE TABLE public.book_genre (
    book_id integer NOT NULL,
    genre_id integer NOT NULL
);
    DROP TABLE public.book_genre;
       public         heap    postgres    false            ?            1259    16521    book_id_seq    SEQUENCE     ?   ALTER TABLE public.book ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.book_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    216            ?            1259    16514    genre    TABLE     `   CREATE TABLE public.genre (
    id integer NOT NULL,
    name character varying(30) NOT NULL
);
    DROP TABLE public.genre;
       public         heap    postgres    false            ?            1259    16513    genre_id_seq    SEQUENCE     ?   ALTER TABLE public.genre ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.genre_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    214                      0    16485    author 
   TABLE DATA           *   COPY public.author (id, name) FROM stdin;
    public          postgres    false    210   %                 0    16522    book 
   TABLE DATA           T   COPY public.book (id, name, price, amount, publication_date, series_id) FROM stdin;
    public          postgres    false    216   ^%                 0    16539 
   book_genre 
   TABLE DATA           7   COPY public.book_genre (book_id, genre_id) FROM stdin;
    public          postgres    false    217   ]&                 0    16514    genre 
   TABLE DATA           )   COPY public.genre (id, name) FROM stdin;
    public          postgres    false    214   ?&                 0    16501    series 
   TABLE DATA           C   COPY public.series (id, name, book_numbers, author_id) FROM stdin;
    public          postgres    false    212   ('                  0    0    Series_series_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public."Series_series_id_seq"', 9, true);
          public          postgres    false    211                       0    0    author_author_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.author_author_id_seq', 4, true);
          public          postgres    false    209                       0    0    book_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.book_id_seq', 16, true);
          public          postgres    false    215                        0    0    genre_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.genre_id_seq', 8, true);
          public          postgres    false    213            p           2606    16491    author author_name_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_name_key UNIQUE (name);
 @   ALTER TABLE ONLY public.author DROP CONSTRAINT author_name_key;
       public            postgres    false    210            r           2606    16489    author author_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.author DROP CONSTRAINT author_pkey;
       public            postgres    false    210            ~           2606    16543    book_genre book_genre_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public.book_genre
    ADD CONSTRAINT book_genre_pkey PRIMARY KEY (book_id, genre_id);
 D   ALTER TABLE ONLY public.book_genre DROP CONSTRAINT book_genre_pkey;
       public            postgres    false    217    217            |           2606    16538    book book_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.book DROP CONSTRAINT book_pkey;
       public            postgres    false    216            x           2606    16520    genre genre_name_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_name_key UNIQUE (name);
 >   ALTER TABLE ONLY public.genre DROP CONSTRAINT genre_name_key;
       public            postgres    false    214            z           2606    16518    genre genre_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.genre DROP CONSTRAINT genre_pkey;
       public            postgres    false    214            t           2606    16507    series series_name_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_name_key UNIQUE (name);
 @   ALTER TABLE ONLY public.series DROP CONSTRAINT series_name_key;
       public            postgres    false    212            v           2606    16505    series series_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.series DROP CONSTRAINT series_pkey;
       public            postgres    false    212            ?           2606    16527    book book_seriesid_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_seriesid_fkey FOREIGN KEY (series_id) REFERENCES public.series(id) ON DELETE CASCADE;
 A   ALTER TABLE ONLY public.book DROP CONSTRAINT book_seriesid_fkey;
       public          postgres    false    216    212    3190            ?           2606    16544     book_genre bookgenre_bookid_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.book_genre
    ADD CONSTRAINT bookgenre_bookid_fkey FOREIGN KEY (book_id) REFERENCES public.book(id) ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.book_genre DROP CONSTRAINT bookgenre_bookid_fkey;
       public          postgres    false    217    3196    216            ?           2606    16549 !   book_genre bookgenre_genreid_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.book_genre
    ADD CONSTRAINT bookgenre_genreid_fkey FOREIGN KEY (genre_id) REFERENCES public.genre(id) ON DELETE CASCADE;
 K   ALTER TABLE ONLY public.book_genre DROP CONSTRAINT bookgenre_genreid_fkey;
       public          postgres    false    3194    217    214                       2606    16508    series series_authorid_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_authorid_fkey FOREIGN KEY (author_id) REFERENCES public.author(id) ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.series DROP CONSTRAINT series_authorid_fkey;
       public          postgres    false    210    3186    212               H   x?3??L?V??/JI??2?.I-?H?S???K?2?t??K?Spɯ?I?2???O??KU?/?I??qqq ?}          ?   x?=?Aj?0EףS?*ɒ?eB???%/?????NKnߑ)??????0̑??b?s??T`%??VH-$2??????S??aNq"T?6??4B??*??P냟ʺ??C?J?cX&?_J???|???w?q??1oK?9????ޓ?k?B?`v??D?K??`?????P???g7~Ǽ?k?e?4Ο?r[???$??	?tʃfdтo??ZfG?@F?D?FJ???c???P?         :   x???  ?e#Z????s.@??	?8?č-???a???N]y^>????L
=         q   x?5?;
A?:?)???U??66nk????an???ߞz	ɡIo?i4?H5?U*?t?-?6??n??8S?>??_?????^?????"sZ[[lj?h?(?????%?         ?   x?%??
?0E?3_1_ 4}?֕Eu?&??M'2i??????9?[?}b:+???y??X?D;?1Y???|Z??J?
,?z?,??)<??X}fj?_8Ba??
Z?????
G???n?v/????䭟?8y???y?Py2/     