import React from 'react';

import { useState } from 'react';
import { Switch } from '@headlessui/react';

import './market-app-main-filter.module.scss';

const filters = [
  {
    id: 1,
    title: 'Office closed on July 2nd',
    href: '#',
    preview:
      'Cum qui rem deleniti. Suscipit in dolor veritatis sequi aut. Vero ut earum quis deleniti. Ut a sunt eum cum ut repudiandae possimus. Nihil ex tempora neque cum consectetur dolores.',
  },
  {
    id: 2,
    title: 'New password policy',
    href: '#',
    preview:
      'Alias inventore ut autem optio voluptas et repellendus. Facere totam quaerat quam quo laudantium cumque eaque excepturi vel. Accusamus maxime ipsam reprehenderit rerum id repellendus rerum. Culpa cum vel natus. Est sit autem mollitia.',
  },
  {
    id: 3,
    title: 'Office closed on July 2nd 1',
    href: '#',
    preview:
      'Tenetur libero voluptatem rerum occaecati qui est molestiae exercitationem. Voluptate quisquam iure assumenda consequatur ex et recusandae. Alias consectetur voluptatibus. Accusamus a ab dicta et. Consequatur quis dignissimos voluptatem nisi.',
  },
  {
    id: 4,
    title: 'Office closed on July 2nd 2',
    href: '#',
    preview: 'Has text libero',
    checkbox: true,
  },
];

function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}
/* eslint-disable-next-line */
export interface MarketAppMainFilterProps {}

export function MarketAppMainFilter(props: MarketAppMainFilterProps) {
  const [enabled, setEnabled] = useState(false);
  return (
    <div className="mt-5 hidden lg:block">
      {/* Filters */}
      <section aria-labelledby="filters-title">
        <div className="rounded-lg bg-white overflow-hidden shadow">
          <div className="p-6">
            <h2
              className="text-base font-medium text-gray-900"
              id="filters-title"
            >
              Filters
            </h2>
            <div className="flow-root mt-6">
              <ul className="-my-5 divide-y divide-gray-200">
                {filters.map((announcement) => (
                  <li key={announcement.id} className="py-5">
                    {!announcement.checkbox && (
                      <div className="relative focus-within:ring-2 focus-within:ring-green-500">
                        <h3 className="text-sm font-semibold text-gray-800">
                          <a
                            href={announcement.href}
                            className="hover:underline focus:outline-none"
                          >
                            {/* Extend touch target to entire panel */}
                            <span
                              className="absolute inset-0"
                              aria-hidden="true"
                            />
                            {announcement.title}
                          </a>
                        </h3>
                        <div className="mt-1 text-sm text-gray-600 line-clamp-2">
                          {/* {announcement.preview} */}
                        </div>
                      </div>
                    )}
                    {announcement.checkbox && (
                      <div className="relative ">
                        <h3 className="text-sm font-semibold text-gray-800">
                          <a
                            href={announcement.href}
                            className="hover:underline focus:outline-none"
                          >
                            {/* Extend touch target to entire panel */}
                            <span
                              className="absolute inset-0"
                              aria-hidden="true"
                            />
                            {announcement.title}
                          </a>
                        </h3>

                        <div className="mt-1 text-sm text-gray-600 line-clamp-2">
                          <Switch.Group as="div" className="flex items-center">
                            <Switch
                              checked={enabled}
                              onChange={setEnabled}
                              className={classNames(
                                enabled ? 'bg-green-600' : 'bg-gray-200',
                                'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
                              )}
                            >
                              <span className="sr-only">
                                {announcement.preview}
                              </span>
                              <span
                                aria-hidden="true"
                                className={classNames(
                                  enabled ? 'translate-x-5' : 'translate-x-0',
                                  'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                                )}
                              />
                            </Switch>
                            <Switch.Label as="span" className="ml-3">
                              <span className="text-sm font-medium text-gray-900">
                                Annual billing{' '}
                              </span>
                              <span className="text-sm text-gray-500">
                                (Save 10%)
                              </span>
                            </Switch.Label>
                          </Switch.Group>
                        </div>
                      </div>
                    )}
                  </li>
                ))}
              </ul>
            </div>
            <div className="mt-6">
              <a
                href="#"
                className="w-full flex justify-center items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 hover:text-white bg-white hover:bg-green-500"
              >
                Update search
              </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default MarketAppMainFilter;
