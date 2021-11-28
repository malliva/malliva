import React, { useEffect } from 'react';

import './market-app-create-listing.module.scss';

import { Menu, Switch, Transition } from '@headlessui/react';
import { useState } from 'react';
import { postCreateListing } from '@client/shared/account-syn-api';
import { useDispatch } from 'react-redux';
import axios from 'axios';

function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}

/* eslint-disable-next-line */
export interface MarketAppCreateListingProps {}

export function MarketAppCreateListing(props: MarketAppCreateListingProps) {
  const dispatch = useDispatch();
  const API_GETPRESIGNEDIMAGEURL_LAMBDA =
    'https://gt9pm8a9b0.execute-api.us-east-2.amazonaws.com/default/getPresignedImageURL';
  const API_CLOUDFRONT = 'https://de1zwyywuzu14.cloudfront.net/';

  const [visible, setVisible] = useState(false);
  const [images, setImages] = useState([]);
  const [listing, setListing] = useState({
    title: '',
    price: '',
    posted_by: '',
    category: '',
    description: '',
    listing_images: [],
  });

  const handleImageUpload = (event) => {
    event.preventDefault();
    const file = event.target;
    uploadFile(file);
  };

  const uploadFile = (event) => {
    const file = event.files[0];
    const fileName = event.files[0].name;
    const reader = new FileReader();
    reader.onloadend = function () {
      const data = (reader.result as string).split(',')[1];
      const binaryBlob = atob(data);
      handleAwsImageUpload(fileName, binaryBlob);
    };
    reader.readAsDataURL(file);
  };

  const handleAwsImageUpload = async (name, binaryBlob) => {
    //https://www.youtube.com/watch?v=_khupEk42zs
    const url =
      'https://9a7gbs3ile.execute-api.us-east-2.amazonaws.com/Prod/image/ ';

    try {
      const data = {
        key: name,
        body: binaryBlob,
      };
      await axios
        .put(url, data)
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    } catch (error) {
      console.log(error);
    }
  };

  const handleListingSubmit = (event) => {
    event.preventDefault();
    const formData = {
      title: listing.title,
      price: listing.price,
      posted_by: listing.posted_by,
      category: listing.category,
      description: listing.description,
      listing_images: listing.listing_images,
      visible: visible,
    };
    dispatch(postCreateListing(formData));
  };

  const handleListingChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;

    setListing((prevalue) => {
      return {
        ...prevalue, // Spread Operator
        [name]: value,
      };
    });
  };

  return (
    <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
      <div className="flex justify-center min-h-screen py-12 sm:px-6 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-md">
          <div className="px-4 py-8 bg-white shadow sm:rounded-lg sm:px-10">
            <h2 className="mb-4 text-3xl font-extrabold text-left text-gray-900">
              Create your listing
            </h2>
            <form className="space-y-6" action="#" method="POST">
              <div>
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-gray-700"
                >
                  Title
                </label>
                <div className="mt-1">
                  <input
                    id="title"
                    name="title"
                    type="text"
                    autoComplete="title"
                    required
                    onChange={handleListingChange}
                    className="block w-full px-3 py-2 placeholder-gray-400 border border-gray-300 rounded-md shadow-sm appearance-none focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="price"
                  className="block text-sm font-medium text-gray-700"
                >
                  Price
                </label>
                <div className="mt-1">
                  <input
                    id="price"
                    name="price"
                    type="text"
                    autoComplete="price"
                    required
                    onChange={handleListingChange}
                    className="block w-full px-3 py-2 placeholder-gray-400 border border-gray-300 rounded-md shadow-sm appearance-none focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="posted_by"
                  className="block text-sm font-medium text-gray-700"
                >
                  Prosted By
                </label>
                <div className="mt-1">
                  <input
                    id="posted_by"
                    name="posted_by"
                    type="text"
                    autoComplete="posted_by"
                    required
                    onChange={handleListingChange}
                    className="block w-full px-3 py-2 placeholder-gray-400 border border-gray-300 rounded-md shadow-sm appearance-none focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="category"
                  className="block text-sm font-medium text-gray-700"
                >
                  Category
                </label>
                <select
                  id="category"
                  name="category"
                  className="block w-full h-full px-3 py-0 py-2 pl-2 text-gray-500 placeholder-gray-400 bg-transparent border border-transparent border-gray-300 rounded-md shadow-sm appearance-none focus:ring-indigo-500 focus:border-indigo-500 pr-7 sm:text-sm"
                  onChange={handleListingChange}
                >
                  <option>USD</option>
                  <option>CAD</option>
                  <option>EUR</option>
                </select>
              </div>

              <div>
                <label
                  htmlFor="posted_by"
                  className="block text-sm font-medium text-gray-700"
                >
                  Detailed description
                </label>
                <div className="mt-1">
                  <textarea
                    name="description"
                    id="description"
                    className="block w-full border border-gray-300 rounded-md shadow-sm resize focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    placeholder="Posting instruction"
                    onChange={handleListingChange}
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="listing_images"
                  className="block text-sm font-medium text-gray-700"
                >
                  Listing images
                </label>
                <div className="mt-1">
                  <input
                    onChange={handleImageUpload}
                    multiple
                    id="listing_images"
                    name="listing_images"
                    type="file"
                    required
                    className="block w-full px-3 py-2 placeholder-gray-400 border border-gray-300 rounded-md shadow-sm appearance-none focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                </div>
              </div>

              <div>
                <div className="flex items-center">
                  <Switch.Group as="div" className="flex items-center">
                    <Switch
                      checked={visible}
                      onChange={setVisible}
                      className={classNames(
                        visible ? 'bg-green-600' : 'bg-gray-200',
                        'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-300'
                      )}
                    >
                      <span
                        aria-hidden="true"
                        className={classNames(
                          visible ? 'translate-x-5' : 'translate-x-0',
                          'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                        )}
                      />
                    </Switch>
                    <Switch.Label as="span" className="ml-2">
                      <a
                        target="blank"
                        href="#"
                        className="text-xs font-medium text-gray-600"
                      >
                        Publish after review
                      </a>
                    </Switch.Label>
                  </Switch.Group>
                </div>
              </div>

              <div>
                <button
                  onClick={handleListingSubmit}
                  type="submit"
                  className="flex justify-center w-full px-4 py-2 text-sm font-medium text-white bg-indigo-600 border border-transparent rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Submit for review
                </button>
              </div>
            </form>
          </div>
        </div>
        <div className="sm:mx-auto sm:w-full sm:max-w-md">
          <div className="p-2 border-4 border-dotted border-light-blue-500">
            All listings on company will be reviewed before publishing. Once
            your listing has been approved, you will be notified by email and it
            will be visible to all.
          </div>
        </div>
      </div>
    </div>
  );
}

export default MarketAppCreateListing;
