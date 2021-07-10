import React, { useState } from 'react';
import { Switch } from '@headlessui/react';

import './market-app-user-rights.module.scss';

/* eslint-disable-next-line */
export interface MarketAppUserRightsProps {}

function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}

export function MarketAppUserRights(props: MarketAppUserRightsProps) {
  const [enabled, setEnabled] = useState(false);
  return (
    <div className="lg:grid grid-cols-12 lg:block lg:col-span-9 xl:col-span-9 lg:gap-8">
      <div className="lg:col-span-12 xl:col-span-12">
        <div className="bg-white px-4 py-5 border-b border-gray-200 sm:px-6">
          <h3 className="text-lg leading-6 font-medium text-gray-900">
            User rights
          </h3>
        </div>
        <div>
          <div>
            <p>Invitation rights</p>
            <p>
              <Switch
                checked={enabled}
                onChange={setEnabled}
                className={classNames(
                  enabled ? 'bg-indigo-600' : 'bg-gray-200',
                  'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                )}
              >
                <span className="sr-only">Use setting</span>
                <span
                  aria-hidden="true"
                  className={classNames(
                    enabled ? 'translate-x-5' : 'translate-x-0',
                    'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                  )}
                />
              </Switch>
              Allow new users to sign up only with an invite from a registered
              user
            </p>
            <p>
              <Switch
                checked={enabled}
                onChange={setEnabled}
                className={classNames(
                  enabled ? 'bg-indigo-600' : 'bg-gray-200',
                  'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                )}
              >
                <span className="sr-only">Use setting</span>
                <span
                  aria-hidden="true"
                  className={classNames(
                    enabled ? 'translate-x-5' : 'translate-x-0',
                    'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                  )}
                />
              </Switch>
              Allow all registered users, and not only admins, to invite new
              users
            </p>
          </div>

          <div>
            <p>Communication rights</p>
            <p>
              <Switch
                checked={enabled}
                onChange={setEnabled}
                className={classNames(
                  enabled ? 'bg-indigo-600' : 'bg-gray-200',
                  'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                )}
              >
                <span className="sr-only">Use setting</span>
                <span
                  aria-hidden="true"
                  className={classNames(
                    enabled ? 'translate-x-5' : 'translate-x-0',
                    'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                  )}
                />
              </Switch>
              Allow users to message each other freely
            </p>
          </div>

          <div>
            <p>Posting rights</p>
            <p>
              <Switch
                checked={enabled}
                onChange={setEnabled}
                className={classNames(
                  enabled ? 'bg-indigo-600' : 'bg-gray-200',
                  'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                )}
              >
                <span className="sr-only">Use setting</span>
                <span
                  aria-hidden="true"
                  className={classNames(
                    enabled ? 'translate-x-5' : 'translate-x-0',
                    'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                  )}
                />
              </Switch>
              Allow only users verified by admins to post listings
              <br />
              Help users understand what is required to be allowed to post
              listings on your marketplace. These instructions will be displayed
              on the new listing form only to users who aren't allowed to post
              listings.
              <br />
              <div>
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-gray-700"
                >
                  Posting rights information text
                </label>
                <div className="mt-1">
                  <input
                    type="text"
                    name="email"
                    id="email"
                    className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                    placeholder="you@example.com"
                  />
                </div>
              </div>
            </p>
          </div>
        </div>

        <button
          type="button"
          className="w-2/12 flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Save changes
        </button>
      </div>
    </div>
  );
}

export default MarketAppUserRights;
