import React, { useState } from 'react';
import ImageGallery from 'react-image-gallery';

import { MarketAppFooter } from '@client/market-app/footer';

import 'react-datepicker/dist/react-datepicker.css';
import DatePicker from 'react-datepicker';

import 'react-image-gallery/styles/scss/image-gallery.scss';
import './market-app-item-details.module.scss';

/* eslint-disable-next-line */
export interface MarketAppItemDetailsProps {}

export function MarketAppItemDetails(props: MarketAppItemDetailsProps) {
  const paymentMethod = false;
  const [startDate, setStartDate] = useState(new Date());
  const images = [
    {
      original: 'https://picsum.photos/id/1018/1000/600/',
      thumbnail: 'https://picsum.photos/id/1018/250/150/',
    },
    {
      original: 'https://picsum.photos/id/1015/1000/600/',
      thumbnail: 'https://picsum.photos/id/1015/250/150/',
    },
    {
      original: 'https://picsum.photos/id/1019/1000/600/',
      thumbnail: 'https://picsum.photos/id/1019/250/150/',
    },
  ];

  return (
    <div>
      <div className="bg-gray-50">
        <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-8 lg:px-4 lg:flex lg:items-center lg:justify-between">
          <h2 className="text-3xl font-extrabold tracking-tight text-gray-900 sm:text-3xl">
            <span className="block">Ready to dive in?</span>
          </h2>
          <div className="mt-8 flex lg:mt-0 lg:flex-shrink-0">
            <div className="inline-flex rounded-md shadow">
              <a
                href="#"
                className="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-green-600 hover:bg-green-700"
              >
                Cart
              </a>
            </div>
          </div>
        </div>
      </div>

      <div className="flex justify-center lg:space-between flex-wrap">
        <div className="w-full lg:w-6/12">
          <ImageGallery
            items={images}
            showBullets={true}
            showIndex={true}
            showThumbnails={true}
            lazyLoad={true}
            showPlayButton={true}
          />
          <div>
            tubes E 182CC ( équivalents 5687 Etc...) mesurés et testés RTC
            (fabrication Philips Heerlen Hollande, codes ID6 ⊿ 4B1 & ID6 ⊿ 3B4),
            mesures sur Triplett 3444A avec minimum bon de 9.8 et nominal neuf
            de 15 = 15.9/16.1 & 13/14. envoi possible en colis blindés via
            Mondial Relay ( 5 euros)
          </div>
        </div>

        <div className="w-full lg:w-3/12">
          {paymentMethod && (
            <div className="buy-panel border-b-2 p-5">
              <p className="text-5xl py-2">$70</p>
              <div className="flex flex-col">
                <p className="text-xl py-2">Delivery method</p>
                <p className="text-xl py-2">Shipping (+$20)</p>
                <a
                  href="#"
                  className="relative text-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
                >
                  Buy
                </a>
              </div>
            </div>
          )}

          {!paymentMethod && (
            <div className="rent-panel border-b-2 p-5">
              <p className="text-5xl py-2">$70</p>
              <div>
                <p className="text-2xl py-2"> From </p>
                <DatePicker
                  selected={startDate}
                  onChange={(date) => setStartDate(date)}
                  className="text-xl"
                />
              </div>
              <div>
                <p className="text-2xl py-2">To </p>
                <DatePicker
                  selected={startDate}
                  onChange={(date) => setStartDate(date)}
                  className="text-xl"
                />
              </div>
              <div className="flex flex-col">
                <p className="text-xl py-2">Delivery method</p>
                <p className="text-xl py-2">Shipping (+$20)</p>
                <a
                  href="#"
                  className="relative text-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
                >
                  Rent
                </a>
              </div>
            </div>
          )}

          <div className="owner-panel border-b-2 p-5 flex">
            <div>
              <img
                className="h-20 w-20"
                src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=2&amp;w=256&amp;h=256&amp;q=80"
                alt=""
              ></img>
            </div>
            <div className="pl-5">
              <p className="pb-2">Seller</p>
              <a
                href="#"
                className="relative inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-gray-600 shadow-sm hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
              >
                Contact
              </a>
            </div>
          </div>
        </div>
      </div>
      <MarketAppFooter />
    </div>
  );
}

export default MarketAppItemDetails;
