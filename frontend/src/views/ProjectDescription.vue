<template>
  <div class="about">
    <h1>Project projectDescription</h1>
    <b-row align-h="center">
      <b-col align-self="center" cols="8" class="m-5">
        <div
          aria-level="2"
          class="
            freebirdFormviewerViewItemsSectionheaderTitle
            freebirdCustomFont
          "
          style="
            font-family: 'Google Sans', Roboto, Helvetica, Arial, sans-serif;
            font-size: medium;
            font-weight: 500;
            letter-spacing: 0.1px;
            line-height: 24px;
            color: rgb(32, 33, 36);
            font-style: normal;
            font-variant-ligatures: normal;
            font-variant-caps: normal;
            orphans: 2;
            text-align: start;
            text-indent: 0px;
            text-transform: none;
            white-space: normal;
            widows: 2;
            word-spacing: 0px;
            -webkit-text-stroke-width: 0px;
            text-decoration-thickness: initial;
            text-decoration-style: initial;
            text-decoration-color: initial;
          "
        >
          Project
        </div>
        <div
          class="freebirdFormviewerViewItemsSectionheaderDescriptionText"
          style="
            font-family: Roboto, Arial, sans-serif;
            font-size: 12px;
            font-weight: 400;
            letter-spacing: 0.3px;
            color: rgb(32, 33, 36);
            line-height: 16.2px;
            margin-top: 0px;
            white-space: pre-wrap;
            font-style: normal;
            font-variant-ligatures: normal;
            font-variant-caps: normal;
            orphans: 2;
            text-align: start;
            text-indent: 0px;
            text-transform: none;
            widows: 2;
            word-spacing: 0px;
            -webkit-text-stroke-width: 0px;
            text-decoration-thickness: initial;
            text-decoration-style: initial;
            text-decoration-color: initial;
          "
        >
          <br />Definition:<br /><br />A web application will be developed to
          scrape the data from a product page of Etsy. Product name, product
          main image link, and product price will be scraped and saved to the
          database.<br /><br />Frontend: The UI Part of the project<br /><br />-
          Input Page: Includes the product link input.<br />- Product Page: The
          details of the product (name, image, price) &nbsp;<br />- Products
          Page: The products in the database should be listed as a table on this
          page.<br /><br />Backend/API: The backend functionality of the
          project<br /><br />- Adding Product Function: Gets the product link as
          an input, scraps the data from the website, saves the data to the
          database, and returns the Product Object (product_id, name, image,
          price)<br />- Product Detail Function: Gets the product_id as input
          and returns the Product Object (product_id, name, image, price)<br />-
          Listing Products Function: Returns all the products in the database as
          an array.<br /><br />Notes:<br /><br />- You can choose the frontend
          tech stack as you want (Pure HTML, Bootstrap, React, Vue.js, etc..)<br />-
          For the backend tech stack choose one of these programming languages:
          Python, PHP or Node.js<br />- For the database choose one of these:
          Mysql, PostgreSQL or MongoDB<br />- You should use Docker for
          initializing the projects.<br />- Upload the project source code to
          the GitHub repository of yours<br /><br />Example:<br /><br />1) If we
          insert links below:<br /><br />-
          <a
            href="https://www.google.com/url?q=https://www.etsy.com/uk/listing/772695061/brass-or-silver-leaf-bookmark-set&sa=D&source=editors&ust=1629729881482000&usg=AFQjCNG6xFPZ0O53qSA1UR_0tF-pmq-hkA"
            >https://www.etsy.com/uk/listing/772695061/brass-or-silver-leaf-bookmark-set</a
          ><br />-
          <a
            href="https://www.google.com/url?q=https://www.etsy.com/uk/listing/593579116/plant-enthusiast-bookmarks&sa=D&source=editors&ust=1629729881482000&usg=AFQjCNHpDYr25l1BWRY1JPXxesllfe-Emw"
            >https://www.etsy.com/uk/listing/593579116/plant-enthusiast-bookmarks</a
          ><br /><br />2) Then the Product table in the database:<br /><br />id
          | name | image |price<br />1 | Brass or Silver Leaf Bookmark Set |
          <a
            href="https://www.google.com/url?q=https://i.etsystatic.com/12149676/r/il/b96248/2959017777/il_794xN.2959017777_t44r.jpg&sa=D&source=editors&ust=1629729881482000&usg=AFQjCNFkUlWhZ_mrMfQR7UabVDonB3r49g"
            >https://i.etsystatic.com/12149676/r/il/b96248/2959017777/il_794xN.2959017777_t44r.jpg</a
          >
          | 9.5<br />2 | Plant Enthusiast bookmarks |
          <a
            href="https://www.google.com/url?q=https://i.etsystatic.com/12149676/r/il/2017f1/1659386185/il_794xN.1659386185_qn4d.jpg&sa=D&source=editors&ust=1629729881482000&usg=AFQjCNF2qwx9tHcsunLvFSGh7FJBxB7azw"
            >https://i.etsystatic.com/12149676/r/il/2017f1/1659386185/il_794xN.1659386185_qn4d.jpg</a
          >
          | 7.95
        </div>
      </b-col>
    </b-row>
  </div>
</template>
